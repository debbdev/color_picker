from Window import TkWindow
import tkinter
import pyautogui as py 
import colour 


class App(TkWindow):
    def __init__(self):
        super().__init__(title="Enhanced Color Picker", width=320, height=280) 
        self.started = False 
        self.title("Color Picker")
        self.ToolWindow()
        self.TopMost()
        self.resizable(False, False)
        self.config(bg="black")
        
        # Create main frame with padding
        self.main_frame = tkinter.Frame(self, bg="black")
        self.main_frame.pack(fill=tkinter.BOTH, expand=True, padx=5, pady=5)
        
        # Mouse coordinates display
        self.coord_label = tkinter.Label(
            self.main_frame, 
            text="Mouse: (0, 0)", 
            bg="black", 
            fg="white", 
            font=("Arial", 9)
        )
        self.coord_label.pack(pady=(0, 5))
        
        # Color preview
        self.color_preview = tkinter.Label(
            self.main_frame,
            text="Color Preview",
            bg="gray",
            fg="black",
            font=("Arial", 12, "bold"),
            relief="raised",
            bd=2,
            height=2
        )
        self.color_preview.pack(fill=tkinter.X, pady=(0, 10))
        
        # Hex section
        self.hex_frame = tkinter.Frame(self.main_frame, bg="black")
        self.hex_frame.pack(fill=tkinter.X, pady=2)
        
        self.labelHex = tkinter.Label(
            self.hex_frame, 
            text="HEX:", 
            bg="black", 
            fg="white", 
            font=("Arial", 10, "bold"),
            width=5,
            anchor="w"
        )
        self.labelHex.pack(side=tkinter.LEFT)
        
        self.entryHex = tkinter.Entry(
            self.hex_frame, 
            font=("Arial", 10), 
            bg="gray20", 
            fg="white", 
            justify="center",
            bd=1
        )
        self.entryHex.pack(side=tkinter.LEFT, fill=tkinter.X, expand=True, padx=(5, 0))
        
        # RGB section
        self.rgb_frame = tkinter.Frame(self.main_frame, bg="black")
        self.rgb_frame.pack(fill=tkinter.X, pady=2)
        
        self.labelRGB = tkinter.Label(
            self.rgb_frame, 
            text="RGB:", 
            bg="black", 
            fg="white", 
            font=("Arial", 10, "bold"),
            width=5,
            anchor="w"
        )
        self.labelRGB.pack(side=tkinter.LEFT)
        
        self.entryRGB = tkinter.Entry(
            self.rgb_frame, 
            font=("Arial", 10), 
            bg="gray20", 
            fg="white", 
            justify="center",
            bd=1
        )
        self.entryRGB.pack(side=tkinter.LEFT, fill=tkinter.X, expand=True, padx=(5, 0))
        
        # Button frame
        self.button_frame = tkinter.Frame(self.main_frame, bg="black")
        self.button_frame.pack(fill=tkinter.X, pady=(10, 0))
        
        # Control button (improved styling)
        self.controlBtn = tkinter.Button(
            self.button_frame,
            font=("Arial", 11, "bold"),
            bg="gray30",
            text="START (Space)",
            fg="white",
            justify="center",
            command=self.start,
            relief="raised",
            bd=2,
            activebackground="gray40",
            activeforeground="white"
        )
        self.controlBtn.pack(side=tkinter.LEFT, fill=tkinter.X, expand=True, padx=(0, 2))
        
        # Copy button
        self.copyBtn = tkinter.Button(
            self.button_frame,
            font=("Arial", 9, "bold"),
            bg="gray30",
            text="Copy HEX",
            fg="white",
            command=self.copy_hex,
            relief="raised",
            bd=2,
            activebackground="gray40",
            activeforeground="white",
            width=10
        )
        self.copyBtn.pack(side=tkinter.LEFT, padx=(2, 0))
        
        # Bind click-to-select for entries
        self.entryHex.bind("<Button-1>", lambda e: self.entryHex.select_range(0, tkinter.END))
        self.entryRGB.bind("<Button-1>", lambda e: self.entryRGB.select_range(0, tkinter.END))
        
        self.current_hex = "#000000"
        self.update()

    def start(self):
        self.started = True
        self.controlBtn.config(command=self.stop, text="STOP (Space)", bg="red3", activebackground="red4") 
        self.RunInterval(self.started)
    
    def stop(self):
        self.started = False
        self.controlBtn.config(command=self.start, text="START (Space)", bg="gray30", activebackground="gray40") 
        self.RunInterval(self.started)

    def copy_hex(self):
        """Copy current hex color to clipboard with visual feedback"""
        try:
            self.clipboard_clear()
            self.clipboard_append(self.current_hex)
            print(f"Copied to clipboard: {self.current_hex}")
            
            # Visual feedback
            original_text = self.copyBtn.cget("text")
            self.copyBtn.config(text="Copied!", bg="green4")
            self.after(1000, lambda: self.copyBtn.config(text=original_text, bg="gray30"))
            
        except Exception as e:
            print(f"Failed to copy: {e}")

    def onKeyPress(self, event):
        print(event) 
        if str(event.keysym).lower() == "space":
            if self.started:
                self.stop() 
            else:
                self.start()
        elif str(event.keysym).lower() == "c" and event.state & 0x4:  # Ctrl+C
            self.copy_hex()

    def invert_hex_color(self, hex_color: str) -> str:
        try:
            hex_color = hex_color.lstrip('#')
            inverted_color = '{:06X}'.format(0xFFFFFF - int(hex_color, 16))
            return f'#{inverted_color}'
        except:
            return "#FFFFFF"

    def get_contrast_color(self, hex_color: str) -> str:
        """Get black or white based on luminance for better readability"""
        try:
            hex_color = hex_color.lstrip('#')
            rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
            # Calculate luminance
            luminance = (0.299 * rgb[0] + 0.587 * rgb[1] + 0.114 * rgb[2]) / 255
            return "#000000" if luminance > 0.5 else "#FFFFFF"
        except:
            return "#FFFFFF"

    def intervalFunc(self):
        if not self.started:
            return
            
        try:
            pos = py.position()
            rgb = py.pixel(pos.x, pos.y)

            # Update mouse coordinates
            self.coord_label.config(text=f"Mouse: ({pos.x}, {pos.y})")

            # Convert to hex
            hex_color = colour.rgb2hex((i/255 for i in rgb))
            self.current_hex = hex_color

            # Get contrast color for better readability
            contrast_color = self.get_contrast_color(hex_color)

            # Update color preview
            self.color_preview.config(
                bg=hex_color, 
                fg=contrast_color,
                text=f"Preview\n{hex_color}"
            )

            # Update hex display
            self.entryHex.delete(0, tkinter.END)
            self.entryHex.insert(0, hex_color)
            self.entryHex.config(bg=hex_color, fg=contrast_color)

            # Update RGB display
            rgb_str = f'rgb({",".join(map(str, rgb))})'
            self.entryRGB.delete(0, tkinter.END)
            self.entryRGB.insert(0, rgb_str)
            self.entryRGB.config(bg=hex_color, fg=contrast_color)

        except Exception as e:
            print(f"Error: {e}")
            # Reset to error state
            self.coord_label.config(text="Mouse: Error")
            self.color_preview.config(bg="gray", fg="black", text="Error\nCan't get color")
            
            for entry in [self.entryHex, self.entryRGB]:
                entry.delete(0, tkinter.END)
                entry.insert(0, "Error")
                entry.config(bg="gray20", fg="white")


if __name__ == "__main__":
    App().mainloop()