# main.py - Complete Mobile OS
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import time
import os
import math
import random
import json
from datetime import datetime
import sys

# Mobile configuration
MOBILE_WIDTH = 800
MOBILE_HEIGHT = 600

class SystemConfiguration:
    """System configuration manager"""
    def __init__(self):
        self.config_file = "system_config.json"
        self.default_config = {
            "theme": "dark",
            "font_size": "medium",
            "animations": True,
            "sound": False,
            "last_user": "User"
        }
        self.load_config()
    
    def load_config(self):
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r') as f:
                    self.config = json.load(f)
            else:
                self.config = self.default_config.copy()
                self.save_config()
        except:
            self.config = self.default_config.copy()
    
    def save_config(self):
        try:
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
        except:
            pass

system_config = SystemConfiguration()

class WindowManager:
    """Window management system"""
    def __init__(self):
        self.windows = []
        self.active_window = None
        
    def add_window(self, window):
        if window not in self.windows:
            self.windows.append(window)
            self.bring_to_front(window)
        
    def bring_to_front(self, window):
        if self.active_window:
            self.lower_window(self.active_window)
        
        self.active_window = window
        
        try:
            window.lift()
        except:
            pass
        
        self.animate_window_focus(window)
    
    def lower_window(self, window):
        try:
            current_alpha = window.attributes('-alpha')
            if current_alpha > 0.8:
                window.attributes('-alpha', 0.8)
        except:
            pass
    
    def animate_window_focus(self, window):
        try:
            original_alpha = window.attributes('-alpha')
            steps = [1.0, 0.95, 1.0]
            
            def animate_step(step_index):
                if step_index < len(steps):
                    window.attributes('-alpha', steps[step_index])
                    window.after(50, lambda: animate_step(step_index + 1))
                else:
                    window.attributes('-alpha', original_alpha)
            
            animate_step(0)
        except:
            pass
    
    def close_window(self, window):
        if window in self.windows:
            self.windows.remove(window)
        
        if self.windows:
            self.bring_to_front(self.windows[-1])

window_manager = WindowManager()

class BootScreen:
    """Boot screen with system diagnostics"""
    def __init__(self, master):
        self.master = master
        self.master.configure(bg='#0a0a0a')
        self.master.geometry(f"{MOBILE_WIDTH}x{MOBILE_HEIGHT}")
        
        self.boot_frame = tk.Frame(master, bg='#0a0a0a')
        self.boot_frame.pack(fill='both', expand=True)
        
        # System logo
        self.logo_canvas = tk.Canvas(self.boot_frame, width=180, height=180,
                                    bg='#0a0a0a', highlightthickness=0)
        self.logo_canvas.pack(pady=80)
        self.draw_logo()
        
        self.title_label = tk.Label(self.boot_frame, text="QUANTUM OS",
                                   font=('Arial', 28, 'bold'),
                                   fg='#00ffaa', bg='#0a0a0a')
        self.title_label.pack(pady=10)
        
        self.version_label = tk.Label(self.boot_frame, text="Mobile Edition | Build 2874",
                                     font=('Arial', 11),
                                     fg='#606060', bg='#0a0a0a')
        self.version_label.pack()
        
        # Progress system
        self.progress_frame = tk.Frame(self.boot_frame, bg='#0a0a0a')
        self.progress_frame.pack(pady=50)
        
        self.progress_bar = tk.Canvas(self.progress_frame, width=350, height=6,
                                     bg='#0a0a0a', highlightthickness=0)
        self.progress_bar.pack()
        
        self.status_label = tk.Label(self.boot_frame, text="",
                                    font=('Arial', 10),
                                    fg='#00ffaa', bg='#0a0a0a')
        self.status_label.pack(pady=15)
        
        self.diagnostics_label = tk.Label(self.boot_frame, text="",
                                         font=('Arial', 9),
                                         fg='#404040', bg='#0a0a0a')
        self.diagnostics_label.pack()
        
        self.start_boot_sequence()
    
    def draw_logo(self):
        self.logo_canvas.delete('all')
        center_x, center_y = 90, 90
        
        # Main logo
        self.logo_canvas.create_oval(25, 25, 155, 155,
                                   outline='#00ffaa', width=3)
        
        # Technical elements
        for i in range(8):
            angle = math.radians(i * 45)
            x1 = center_x + 40 * math.cos(angle)
            y1 = center_y + 40 * math.sin(angle)
            x2 = center_x + 60 * math.cos(angle)
            y2 = center_y + 60 * math.sin(angle)
            
            self.logo_canvas.create_line(x1, y1, x2, y2,
                                       fill='#00ffaa', width=2)
        
        # Center
        self.logo_canvas.create_oval(80, 80, 100, 100,
                                   fill='#00ffaa', outline='')
    
    def start_boot_sequence(self):
        boot_steps = [
            ("Initializing system kernel", 15, "Kernel 6.2.0 loaded"),
            ("Loading hardware drivers", 35, "Drivers initialized"),
            ("Mounting file systems", 55, "Storage systems ready"),
            ("Starting core services", 75, "Services operational"),
            ("Initializing security", 90, "Security layer active"),
            ("Loading desktop environment", 100, "System ready")
        ]
        
        def update_progress(step):
            if step < len(boot_steps):
                text, progress, diag = boot_steps[step]
                self.update_progress_display(progress, text, diag)
                self.master.after(700, lambda: update_progress(step + 1))
            else:
                self.master.after(800, self.complete_boot)
        
        update_progress(0)
    
    def update_progress_display(self, progress, text, diagnostic):
        self.progress_bar.delete('progress')
        progress_width = (progress / 100) * 350
        
        self.progress_bar.create_rectangle(0, 0, progress_width, 6,
                                         fill='#00ffaa', outline='', tags='progress')
        
        self.status_label.config(text=text)
        self.diagnostics_label.config(text=diagnostic)
        
        self.animate_logo(progress)
    
    def animate_logo(self, progress):
        self.logo_canvas.delete('animation')
        center_x, center_y = 90, 90
        
        pulse_radius = 40 + (math.sin(time.time() * 3) * 5)
        self.logo_canvas.create_oval(center_x-pulse_radius, center_y-pulse_radius,
                                   center_x+pulse_radius, center_y+pulse_radius,
                                   outline='#004400', width=1, tags='animation')
    
    def complete_boot(self):
        self.transition_to_desktop()
    
    def transition_to_desktop(self):
        def fade_out():
            try:
                current_y = self.boot_frame.winfo_y()
                if current_y > -MOBILE_HEIGHT:
                    new_y = current_y - 20
                    self.boot_frame.place(y=new_y)
                    self.master.after(15, fade_out)
                else:
                    self.boot_frame.destroy()
                    Desktop(self.master)
            except:
                self.boot_frame.destroy()
                Desktop(self.master)
        
        fade_out()

class Desktop:
    """Desktop environment"""
    def __init__(self, master):
        self.master = master
        self.master.configure(bg='#1a1a1a')
        
        self.desktop_frame = tk.Frame(master, bg='#1a1a1a')
        self.desktop_frame.pack(fill='both', expand=True)
        
        self.setup_desktop()
        self.start_services()
    
    def setup_desktop(self):
        self.create_wallpaper()
        self.create_taskbar()
        self.create_app_launcher()
    
    def create_wallpaper(self):
        self.wallpaper_canvas = tk.Canvas(self.desktop_frame, bg='#1a1a1a',
                                         highlightthickness=0)
        self.wallpaper_canvas.pack(fill='both', expand=True)
        
        self.draw_wallpaper()
    
    def draw_wallpaper(self):
        self.wallpaper_canvas.delete('wallpaper')
        width = MOBILE_WIDTH
        height = MOBILE_HEIGHT
        
        # Animated gradient
        for i in range(0, height, 2):
            ratio = i / height
            r = int(20 + math.sin(time.time() * 0.3 + ratio) * 10)
            g = int(30 + math.cos(time.time() * 0.5 + ratio) * 15)
            b = int(40 + math.sin(time.time() * 0.7 + ratio) * 20)
            color = f'#{r:02x}{g:02x}{b:02x}'
            self.wallpaper_canvas.create_line(0, i, width, i, fill=color,
                                            tags='wallpaper')
        
        # System info
        current_time = datetime.now().strftime("%H:%M")
        self.wallpaper_canvas.create_text(width//2, height//2 - 30,
                                         text=current_time,
                                         font=('Arial', 42, 'bold'),
                                         fill='#ffffff', tags='wallpaper')
        
        self.wallpaper_canvas.create_text(width//2, height//2 + 20,
                                         text="Quantum OS Mobile",
                                         font=('Arial', 16),
                                         fill='#888888', tags='wallpaper')
        
        self.master.after(100, self.draw_wallpaper)
    
    def create_taskbar(self):
        self.taskbar = tk.Frame(self.master, bg='#252525', height=70)
        self.taskbar.pack(side='bottom', fill='x')
        self.taskbar.pack_propagate(False)
        
        # App launcher
        self.app_btn = tk.Button(self.taskbar, text="Apps",
                               command=self.show_app_menu,
                               font=('Arial', 12, 'bold'),
                               bg='#00ffaa', fg='#000000',
                               relief='flat', padx=20)
        self.app_btn.pack(side='left', padx=15, pady=15)
        
        # Navigation
        nav_frame = tk.Frame(self.taskbar, bg='#252525')
        nav_frame.pack(side='left', padx=20)
        
        tk.Button(nav_frame, text="Desktop",
                 command=self.show_desktop,
                 font=('Arial', 10),
                 bg='#353535', fg='white',
                 width=8).pack(side='left', padx=5)
        
        # System info
        info_frame = tk.Frame(self.taskbar, bg='#252525')
        info_frame.pack(side='right', padx=15, pady=10)
        
        self.clock_label = tk.Label(info_frame, text="",
                                   font=('Arial', 14, 'bold'),
                                   bg='#252525', fg='#00ffaa')
        self.clock_label.pack()
        
        self.date_label = tk.Label(info_frame, text="",
                                  font=('Arial', 10),
                                  bg='#252525', fg='#888888')
        self.date_label.pack()
        
        self.update_clock()
    
    def update_clock(self):
        now = datetime.now()
        self.clock_label.config(text=now.strftime("%H:%M"))
        self.date_label.config(text=now.strftime("%m/%d/%Y"))
        self.master.after(30000, self.update_clock)
    
    def create_app_launcher(self):
        app_frame = tk.Frame(self.desktop_frame, bg='', bd=0)
        app_frame.place(relx=0.5, rely=0.45, anchor='center')
        
        apps = [
            ("Text Editor", self.open_editor, "#00ffaa"),
            ("Media Player", self.open_media, "#ff6b6b"),
            ("Calculator", self.open_calc, "#4ecdc4"),
            ("Browser", self.open_browser, "#45b7d1"),
            ("File Manager", self.open_files, "#6c5ce7"),
            ("System Info", self.open_system, "#a29bfe"),
            ("Settings", self.open_settings, "#fd79a8")
        ]
        
        for i, (name, command, color) in enumerate(apps):
            row = i // 4
            col = i % 4
            
            app_widget = self.create_app_widget(app_frame, name, color, command)
            app_widget.grid(row=row, column=col, padx=10, pady=10)
    
    def create_app_widget(self, parent, name, color, command):
        frame = tk.Frame(parent, bg='#252525', width=80, height=90,
                        relief='raised', bd=1)
        frame.pack_propagate(False)
        
        # App icon
        icon_canvas = tk.Canvas(frame, width=40, height=40,
                               bg=color, highlightthickness=0)
        icon_canvas.pack(pady=12)
        self.draw_app_icon(icon_canvas, name)
        
        # App name
        name_label = tk.Label(frame, text=name,
                             font=('Arial', 8),
                             bg='#252525', fg='white',
                             wraplength=70)
        name_label.pack()
        
        # Bind clicks
        for child in frame.winfo_children() + [frame]:
            child.bind('<Button-1>', lambda e, cmd=command: cmd())
        
        return frame
    
    def draw_app_icon(self, canvas, app_name):
        canvas.delete('all')
        
        if "Text" in app_name:
            canvas.create_rectangle(8, 8, 32, 32, outline='white', width=2)
            canvas.create_line(10, 15, 30, 15, fill='white', width=2)
            canvas.create_line(10, 20, 30, 20, fill='white', width=2)
            canvas.create_line(10, 25, 22, 25, fill='white', width=2)
        elif "Media" in app_name:
            canvas.create_oval(8, 8, 32, 32, outline='white', width=2)
            canvas.create_oval(15, 15, 25, 25, outline='white', width=2)
        elif "Calculator" in app_name:
            canvas.create_rectangle(8, 8, 32, 32, outline='white', width=2)
            canvas.create_text(20, 20, text="=", font=('Arial', 12, 'bold'), fill='white')
        elif "Browser" in app_name:
            canvas.create_oval(6, 6, 34, 34, outline='white', width=2)
            canvas.create_line(6, 20, 34, 20, fill='white', width=2)
        elif "File" in app_name:
            canvas.create_rectangle(10, 6, 30, 34, outline='white', width=2)
            canvas.create_line(10, 15, 30, 15, fill='white', width=1)
            canvas.create_line(10, 22, 30, 22, fill='white', width=1)
        elif "System" in app_name:
            points = [10, 25, 15, 15, 20, 20, 25, 10, 30, 25]
            canvas.create_line(points, fill='white', width=2, smooth=True)
        elif "Settings" in app_name:
            canvas.create_oval(10, 10, 30, 30, outline='white', width=2)
            for i in range(4):
                angle = math.radians(i * 90)
                x1 = 20 + 8 * math.cos(angle)
                y1 = 20 + 8 * math.sin(angle)
                x2 = 20 + 4 * math.cos(angle)
                y2 = 20 + 4 * math.sin(angle)
                canvas.create_line(x1, y1, x2, y2, fill='white', width=2)
    
    def show_app_menu(self):
        AppMenu(self.master)
    
    def show_desktop(self):
        for window in window_manager.windows[:]:
            window_manager.close_window(window)
    
    def start_services(self):
        print("System services running")
    
    def open_editor(self):
        TextEditor(self.master)
    
    def open_media(self):
        MediaPlayer(self.master)
    
    def open_calc(self):
        Calculator(self.master)
    
    def open_browser(self):
        WebBrowser(self.master)
    
    def open_files(self):
        FileManager(self.master)
    
    def open_system(self):
        SystemInfo(self.master)
    
    def open_settings(self):
        Settings(self.master)

class AppMenu:
    """Application menu"""
    def __init__(self, master):
        self.master = master
        self.create_menu()
    
    def create_menu(self):
        self.menu = tk.Toplevel(self.master)
        self.menu.configure(bg='#252525')
        self.menu.overrideredirect(True)
        
        menu_width = MOBILE_WIDTH - 100
        menu_height = 350
        x = (MOBILE_WIDTH - menu_width) // 2
        y = MOBILE_HEIGHT - menu_height - 70
        
        self.menu.geometry(f"{menu_width}x{menu_height}+{x}+{y}")
        self.menu.attributes('-alpha', 0.0)
        
        self.build_menu()
        self.animate_open()
    
    def build_menu(self):
        # Header
        header = tk.Frame(self.menu, bg='#00ffaa', height=50)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        tk.Label(header, text="Applications",
                font=('Arial', 16, 'bold'),
                bg='#00ffaa', fg='#000000').pack(pady=15)
        
        # Apps list
        container = tk.Frame(self.menu, bg='#252525')
        container.pack(fill='both', expand=True, padx=10, pady=10)
        
        apps = [
            ("Text Editor", self.open_editor),
            ("Media Player", self.open_media),
            ("Calculator", self.open_calc),
            ("Web Browser", self.open_browser),
            ("File Manager", self.open_files),
            ("System Info", self.open_system),
            ("Settings", self.open_settings),
            ("Shutdown", self.shutdown)
        ]
        
        for name, command in apps:
            btn = tk.Button(container, text=name, font=('Arial', 12),
                          bg='#353535', fg='white', width=20,
                          command=command, anchor='w')
            btn.pack(pady=2, fill='x')
    
    def animate_open(self):
        alpha = 0.0
        def fade_in():
            nonlocal alpha
            if alpha < 0.95:
                alpha += 0.1
                self.menu.attributes('-alpha', alpha)
                self.menu.after(20, fade_in)
        fade_in()
        
        self.menu.focus_force()
        self.menu.bind('<Button-1>', self.check_click)
    
    def check_click(self, event):
        if event.widget == self.menu:
            self.animate_close()
    
    def animate_close(self):
        alpha = 0.95
        def fade_out():
            nonlocal alpha
            if alpha > 0:
                alpha -= 0.1
                self.menu.attributes('-alpha', alpha)
                self.menu.after(20, fade_out)
            else:
                self.menu.destroy()
        fade_out()
    
    def open_editor(self):
        TextEditor(self.master)
        self.animate_close()
    
    def open_media(self):
        MediaPlayer(self.master)
        self.animate_close()
    
    def open_calc(self):
        Calculator(self.master)
        self.animate_close()
    
    def open_browser(self):
        WebBrowser(self.master)
        self.animate_close()
    
    def open_files(self):
        FileManager(self.master)
        self.animate_close()
    
    def open_system(self):
        SystemInfo(self.master)
        self.animate_close()
    
    def open_settings(self):
        Settings(self.master)
        self.animate_close()
    
    def shutdown(self):
        self.animate_close()
        ShutdownDialog(self.master)

class WindowBase:
    """Base window class"""
    def __init__(self, master, title, width=None, height=None):
        if width is None:
            width = min(MOBILE_WIDTH - 50, 600)
        if height is None:
            height = min(MOBILE_HEIGHT - 100, 500)
            
        self.window = tk.Toplevel(master)
        self.window.title(title)
        self.window.configure(bg='#252525')
        self.window.attributes('-alpha', 0.0)
        
        x = (MOBILE_WIDTH - width) // 2
        y = (MOBILE_HEIGHT - height) // 2
        self.window.geometry(f"{width}x{height}+{x}+{y}")
        
        self.create_interface(title)
        window_manager.add_window(self.window)
        
        self.animate_open()
    
    def create_interface(self, title):
        # Title bar
        self.title_bar = tk.Frame(self.window, bg='#00ffaa', height=45)
        self.title_bar.pack(fill='x')
        self.title_bar.pack_propagate(False)
        
        tk.Label(self.title_bar, text=title,
                font=('Arial', 13, 'bold'),
                bg='#00ffaa', fg='#000000').pack(side='left', padx=15, pady=12)
        
        # Controls
        controls = tk.Frame(self.title_bar, bg='#00ffaa')
        controls.pack(side='right', padx=5)
        
        tk.Button(controls, text="—",
                 command=self.minimize,
                 font=('Arial', 12),
                 bg='#00aa88', fg='white',
                 width=3, relief='flat').pack(side='left', padx=2)
        
        tk.Button(controls, text="✕",
                 command=self.animate_close,
                 font=('Arial', 10),
                 bg='#ff4444', fg='white',
                 width=3, relief='flat').pack(side='left', padx=2)
        
        # Content
        self.content = tk.Frame(self.window, bg='#252525')
        self.content.pack(fill='both', expand=True)
    
    def animate_open(self):
        alpha = 0.0
        def fade_in():
            nonlocal alpha
            if alpha < 1.0:
                alpha += 0.1
                self.window.attributes('-alpha', alpha)
                self.window.after(20, fade_in)
        fade_in()
    
    def animate_close(self):
        alpha = 1.0
        def fade_out():
            nonlocal alpha
            if alpha > 0:
                alpha -= 0.1
                self.window.attributes('-alpha', alpha)
                self.window.after(20, fade_out)
            else:
                window_manager.close_window(self.window)
                self.window.destroy()
        fade_out()
    
    def minimize(self):
        self.window.withdraw()

# Application implementations
class TextEditor(WindowBase):
    def __init__(self, master):
        super().__init__(master, "Text Editor", 700, 500)
        
        # Toolbar
        toolbar = tk.Frame(self.content, bg='#353535', height=40)
        toolbar.pack(fill='x', padx=5, pady=5)
        toolbar.pack_propagate(False)
        
        for text, command in [("New", self.new_file),
                            ("Open", self.open_file),
                            ("Save", self.save_file)]:
            tk.Button(toolbar, text=text, command=command,
                     font=('Arial', 10), bg='#00ffaa', fg='black').pack(side='left', padx=5)
        
        # Text area
        self.text_area = scrolledtext.ScrolledText(self.content,
                                                  font=('Arial', 12),
                                                  bg='#1a1a1a', fg='#ffffff',
                                                  insertbackground='white',
                                                  padx=15, pady=15)
        self.text_area.pack(fill='both', expand=True, padx=5, pady=5)
        
        # Status
        self.status = tk.Label(self.content, text="Ready",
                              font=('Arial', 9),
                              bg='#353535', fg='#888888',
                              anchor='w')
        self.status.pack(fill='x', side='bottom')
        
        self.current_file = None
        self.text_area.focus()
    
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        self.status.config(text="New Document")
    
    def save_file(self):
        try:
            content = self.text_area.get(1.0, tk.END)
            filename = "document.txt"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            self.current_file = filename
            self.status.config(text=f"Saved: {filename}")
            messagebox.showinfo("Success", "Document saved successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Save failed: {str(e)}")
    
    def open_file(self):
        try:
            filename = "document.txt"
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as f:
                    content = f.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, content)
                self.current_file = filename
                self.status.config(text=f"Loaded: {filename}")
            else:
                messagebox.showinfo("Info", "No previous document found")
        except Exception as e:
            messagebox.showerror("Error", f"Open failed: {str(e)}")

class MediaPlayer(WindowBase):
    def __init__(self, master):
        super().__init__(master, "Media Player", 400, 350)
        
        self.playing = False
        self.current_track = 0
        self.playlist = [
            "Classical Symphony",
            "Ambient Sounds", 
            "Electronic Beats"
        ]
        
        # Display
        display = tk.Frame(self.content, bg='#1a1a1a')
        display.pack(fill='x', padx=20, pady=20)
        
        self.visual = tk.Canvas(display, width=120, height=120,
                               bg='#0a0a0a', highlightthickness=0)
        self.visual.pack(pady=10)
        self.draw_visual()
        
        self.track_label = tk.Label(display,
                                   text=self.playlist[self.current_track],
                                   font=('Arial', 12, 'bold'),
                                   bg='#1a1a1a', fg='#ffffff')
        self.track_label.pack(pady=5)
        
        self.status_label = tk.Label(display, text="Stopped",
                                    font=('Arial', 10),
                                    bg='#1a1a1a', fg='#00ffaa')
        self.status_label.pack()
        
        # Progress
        self.progress = ttk.Progressbar(self.content, length=300, mode='determinate')
        self.progress.pack(pady=10)
        
        # Controls
        controls = tk.Frame(self.content, bg='#252525')
        controls.pack(pady=15)
        
        tk.Button(controls, text="|<", font=('Arial', 12), width=4,
                 command=self.previous_track).pack(side='left', padx=5)
        
        self.play_btn = tk.Button(controls, text=">", font=('Arial', 14), width=4,
                                 command=self.toggle_play)
        self.play_btn.pack(side='left', padx=10)
        
        tk.Button(controls, text=">|", font=('Arial', 12), width=4,
                 command=self.next_track).pack(side='left', padx=5)
        
        self.simulate_playback()
    
    def draw_visual(self):
        self.visual.delete('all')
        
        center_x, center_y = 60, 60
        for i in range(12):
            angle = math.radians(i * 30)
            height = random.randint(10, 40)
            x1 = center_x + 35 * math.cos(angle)
            y1 = center_y + 35 * math.sin(angle)
            x2 = center_x + (35 + height) * math.cos(angle)
            y2 = center_y + (35 + height) * math.sin(angle)
            
            color = '#00ffaa' if self.playing else '#444444'
            self.visual.create_line(x1, y1, x2, y2, fill=color, width=3)
    
    def toggle_play(self):
        self.playing = not self.playing
        if self.playing:
            self.status_label.config(text="Playing")
            self.play_btn.config(text="||")
        else:
            self.status_label.config(text="Paused")
            self.play_btn.config(text=">")
        
        self.draw_visual()
    
    def previous_track(self):
        self.current_track = (self.current_track - 1) % len(self.playlist)
        self.track_label.config(text=self.playlist[self.current_track])
        self.progress['value'] = 0
    
    def next_track(self):
        self.current_track = (self.current_track + 1) % len(self.playlist)
        self.track_label.config(text=self.playlist[self.current_track])
        self.progress['value'] = 0
    
    def simulate_playback(self):
        if self.playing and self.progress['value'] < 100:
            self.progress['value'] += 0.5
            self.draw_visual()
        self.window.after(100, self.simulate_playback)

class Calculator(WindowBase):
    def __init__(self, master):
        super().__init__(master, "Calculator", 300, 400)
        
        self.display_var = tk.StringVar(value="0")
        
        # Display
        display = tk.Entry(self.content, textvariable=self.display_var,
                          font=('Arial', 20), justify='right',
                          bg='#1a1a1a', fg='white', bd=0)
        display.pack(fill='x', padx=10, pady=10, ipady=10)
        
        # Buttons
        buttons = [
            ['C', '±', '%', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '', '.', '=']
        ]
        
        button_frame = tk.Frame(self.content, bg='#252525')
        button_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                if text:
                    btn = tk.Button(button_frame, text=text,
                                  font=('Arial', 14),
                                  bg='#353535' if text not in ['÷', '×', '-', '+', '='] else '#00aa88',
                                  fg='white',
                                  command=lambda t=text: self.button_click(t))
                    btn.grid(row=i, column=j, sticky='nsew', padx=2, pady=2)
                    
                    if text == '0':
                        btn.grid(columnspan=2, sticky='nsew')
        
        # Configure grid
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.grid_columnconfigure(j, weight=1)
        
        self.reset_calc()
    
    def reset_calc(self):
        self.current = "0"
        self.previous = ""
        self.operator = ""
        self.display_var.set("0")
    
    def button_click(self, text):
        if text in '0123456789':
            if self.current == "0":
                self.current = text
            else:
                self.current += text
            self.display_var.set(self.current)
        
        elif text == '.':
            if '.' not in self.current:
                self.current += '.'
                self.display_var.set(self.current)
        
        elif text in ['+', '-', '×', '÷']:
            self.previous = self.current
            self.current = "0"
            self.operator = text
        
        elif text == '=':
            if self.operator and self.previous:
                try:
                    num1 = float(self.previous)
                    num2 = float(self.current)
                    
                    if self.operator == '+':
                        result = num1 + num2
                    elif self.operator == '-':
                        result = num1 - num2
                    elif self.operator == '×':
                        result = num1 * num2
                    elif self.operator == '÷':
                        result = num1 / num2 if num2 != 0 else "Error"
                    
                    self.display_var.set(str(result))
                    self.current = str(result)
                    self.operator = ""
                except:
                    self.display_var.set("Error")
                    self.current = "0"
        
        elif text == 'C':
            self.reset_calc()
        
        elif text == '±':
            if self.current and self.current != "0":
                if self.current[0] == '-':
                    self.current = self.current[1:]
                else:
                    self.current = '-' + self.current
                self.display_var.set(self.current)

class WebBrowser(WindowBase):
    def __init__(self, master):
        super().__init__(master, "Web Browser", 700, 500)
        
        # Address bar
        address_frame = tk.Frame(self.content, bg='#353535')
        address_frame.pack(fill='x', padx=10, pady=10)
        
        self.url_var = tk.StringVar(value="https://quantum-os.com")
        url_entry = tk.Entry(address_frame, textvariable=self.url_var,
                            font=('Arial', 12), bg='#1a1a1a', fg='white')
        url_entry.pack(side='left', fill='x', expand=True, padx=(0, 10))
        
        tk.Button(address_frame, text="Go", command=self.load_page,
                 font=('Arial', 10)).pack(side='right')
        
        # Content
        content_frame = tk.Frame(self.content, bg='#252525')
        content_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.content_text = scrolledtext.ScrolledText(content_frame,
                                                     font=('Arial', 11),
                                                     bg='white', fg='black')
        self.content_text.pack(fill='both', expand=True)
        
        self.load_page()
    
    def load_page(self):
        self.content_text.delete(1.0, tk.END)
        self.content_text.insert(1.0, f"QUANTUM OS WEB BROWSER\n\n")
        self.content_text.insert(tk.END, f"Address: {self.url_var.get()}\n\n")
        self.content_text.insert(tk.END, "Welcome to Quantum OS Browser!\n\n")
        self.content_text.insert(tk.END, "This is a simulated browser for demonstration.\n")
        self.content_text.insert(tk.END, "All web functionality is simulated for this prototype.")

class FileManager(WindowBase):
    def __init__(self, master):
        super().__init__(master, "File Manager", 600, 400)
        
        # Address bar
        address_frame = tk.Frame(self.content, bg='#353535')
        address_frame.pack(fill='x', padx=10, pady=10)
        
        self.path_var = tk.StringVar(value=os.getcwd())
        tk.Label(address_frame, textvariable=self.path_var,
                font=('Arial', 10), bg='#353535', fg='white').pack(side='left')
        
        tk.Button(address_frame, text="Refresh", command=self.refresh_files,
                 font=('Arial', 10)).pack(side='right')
        
        # File list
        self.file_list = tk.Listbox(self.content, font=('Arial', 12),
                                   bg='#1a1a1a', fg='white',
                                   selectbackground='#00ffaa')
        self.file_list.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.refresh_files()
    
    def refresh_files(self):
        self.file_list.delete(0, tk.END)
        try:
            files = os.listdir(self.path_var.get())
            for file in files:
                self.file_list.insert(tk.END, file)
        except Exception as e:
            messagebox.showerror("Error", f"Cannot access: {str(e)}")

class SystemInfo(WindowBase):
    def __init__(self, master):
        super().__init__(master, "System Information", 350, 400)
        
        info_frame = tk.Frame(self.content, bg='#252525')
        info_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # System info
        infos = [
            ("OS", "Quantum OS Mobile"),
            ("Version", "2.1.0"),
            ("Screen", f"{MOBILE_WIDTH}x{MOBILE_HEIGHT}"),
            ("Python", "3.x"),
            ("Status", "Normal"),
            ("Uptime", "00:00:00")
        ]
        
        for i, (label, value) in enumerate(infos):
            tk.Label(info_frame, text=label + ":", font=('Arial', 10, 'bold'),
                    bg='#252525', fg='#00ffaa').grid(row=i, column=0, sticky='w', pady=5)
            tk.Label(info_frame, text=value, font=('Arial', 10),
                    bg='#252525', fg='white').grid(row=i, column=1, sticky='w', pady=5)
        
        # Usage graph
        self.usage_canvas = tk.Canvas(self.content, width=300, height=100,
                                     bg='#1a1a1a', highlightthickness=0)
        self.usage_canvas.pack(pady=20)
        
        self.update_usage()
    
    def update_usage(self):
        self.usage_canvas.delete('all')
        
        # Simulate system usage
        usage = random.randint(10, 80)
        
        # Draw graph
        self.usage_canvas.create_rectangle(50, 50, 50 + usage * 2, 80, fill='#00ffaa')
        self.usage_canvas.create_text(150, 30, text=f"System Usage: {usage}%", 
                                     font=('Arial', 12), fill='white')
        
        self.window.after(2000, self.update_usage)

class Settings(WindowBase):
    def __init__(self, master):
        super().__init__(master, "System Settings", 350, 400)
        
        container = tk.Frame(self.content, bg='#252525')
        container.pack(fill='both', expand=True, padx=20, pady=20)
        
        settings = [
            ("Theme", ["Dark", "Light", "Auto"]),
            ("Font Size", ["Small", "Medium", "Large"]),
            ("Animation", ["On", "Off"]),
            ("Sound", ["On", "Off"]),
        ]
        
        for i, (label, options) in enumerate(settings):
            tk.Label(container, text=label, font=('Arial', 12),
                    bg='#252525', fg='white').grid(row=i, column=0, sticky='w', pady=10)
            
            var = tk.StringVar(value=options[0])
            dropdown = ttk.Combobox(container, textvariable=var, values=options,
                                   state='readonly', width=12)
            dropdown.grid(row=i, column=1, sticky='e', pady=10)
        
        # Action buttons
        action_frame = tk.Frame(container, bg='#252525')
        action_frame.grid(row=len(settings), column=0, columnspan=2, pady=20)
        
        tk.Button(action_frame, text="Save", command=self.save_settings,
                 bg='#00ffaa', fg='black', font=('Arial', 12)).pack(side='left', padx=10)
        
        tk.Button(action_frame, text="Reset", command=self.reset_settings,
                 bg='#ff4444', fg='white', font=('Arial', 12)).pack(side='left', padx=10)
    
    def save_settings(self):
        messagebox.showinfo("Settings", "Settings saved successfully!")
    
    def reset_settings(self):
        if messagebox.askyesno("Reset", "Reset all settings to default?"):
            messagebox.showinfo("Settings", "Settings reset successfully!")

class ShutdownDialog:
    def __init__(self, master):
        self.master = master
        self.create_dialog()
    
    def create_dialog(self):
        self.dialog = tk.Toplevel(self.master)
        self.dialog.configure(bg='#1a1a1a')
        self.dialog.overrideredirect(True)
        self.dialog.attributes('-alpha', 0.0)
        
        width, height = 320, 200
        x = (MOBILE_WIDTH - width) // 2
        y = (MOBILE_HEIGHT - height) // 2
        self.dialog.geometry(f"{width}x{height}+{x}+{y}")
        
        # Content
        tk.Label(self.dialog, text="System Shutdown",
                font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='#ff4444').pack(pady=20)
        
        tk.Label(self.dialog, text="Are you sure you want to shutdown?",
                font=('Arial', 10),
                bg='#1a1a1a', fg='#888888').pack(pady=10)
        
        # Buttons
        button_frame = tk.Frame(self.dialog, bg='#1a1a1a')
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="Cancel",
                 command=self.cancel,
                 font=('Arial', 12),
                 bg='#00ffaa', fg='black',
                 width=10).pack(side='left', padx=10)
        
        tk.Button(button_frame, text="Shutdown",
                 command=self.confirm,
                 font=('Arial', 12),
                 bg='#ff4444', fg='white',
                 width=10).pack(side='left', padx=10)
        
        self.animate_in()
    
    def animate_in(self):
        alpha = 0.0
        def fade_in():
            nonlocal alpha
            if alpha < 1.0:
                alpha += 0.1
                self.dialog.attributes('-alpha', alpha)
                self.dialog.after(20, fade_in)
        fade_in()
    
    def cancel(self):
        self.animate_out()
    
    def confirm(self):
        self.shutdown()
    
    def animate_out(self):
        alpha = 1.0
        def fade_out():
            nonlocal alpha
            if alpha > 0:
                alpha -= 0.1
                self.dialog.attributes('-alpha', alpha)
                self.dialog.after(20, fade_out)
            else:
                self.dialog.destroy()
        fade_out()
    
    def shutdown(self):
        shutdown_win = tk.Toplevel(self.master)
        shutdown_win.attributes('-fullscreen', True, '-alpha', 0.0)
        shutdown_win.configure(bg='black')
        shutdown_win.overrideredirect(True)
        
        canvas = tk.Canvas(shutdown_win, bg='black', highlightthickness=0)
        canvas.pack(fill='both', expand=True)
        
        def shutdown_seq(step):
            if step == 0:
                canvas.create_text(MOBILE_WIDTH//2, MOBILE_HEIGHT//2,
                                 text="System shutting down...",
                                 font=('Arial', 18),
                                 fill='white')
                shutdown_win.attributes('-alpha', 1.0)
                shutdown_win.after(1000, lambda: shutdown_seq(1))
            elif step == 1:
                canvas.delete('all')
                canvas.create_text(MOBILE_WIDTH//2, MOBILE_HEIGHT//2,
                                 text="Goodbye",
                                 font=('Arial', 24),
                                 fill='white')
                shutdown_win.after(1000, lambda: shutdown_seq(2))
            else:
                self.master.quit()
        
        self.animate_out()
        shutdown_seq(0)

# Start system
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quantum OS Mobile")
    root.geometry(f"{MOBILE_WIDTH}x{MOBILE_HEIGHT}")
    root.resizable(False, False)
    
    BootScreen(root)
    root.mainloop()