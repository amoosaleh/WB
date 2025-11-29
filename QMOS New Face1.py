# main.py - Complete Mobile OS with All Games Working
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog, simpledialog
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

class TouchOptimizer:
    """Touch event optimizer for mobile"""
    @staticmethod
    def make_touch_friendly(widget):
        """Make widget touch-friendly"""
        if isinstance(widget, tk.Button):
            widget.config(
                relief='flat',
                borderwidth=4,
                padx=20,
                pady=12,
                font=('Arial', 12),
                cursor='hand2'
            )

class SystemConfiguration:
    """System configuration manager"""
    def __init__(self):
        self.config_file = "quantum_config.json"
        self.default_config = {
            "theme": "quantum",
            "font_size": "medium",
            "animations": True,
            "sound": True,
            "user_name": "Quantum User",
            "high_score": 0,
            "wallpaper": "dynamic"
        }
        self.load_config()
    
    def load_config(self):
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    self.config = json.load(f)
            else:
                self.config = self.default_config.copy()
                self.save_config()
        except Exception as e:
            print(f"Config load error: {e}")
            self.config = self.default_config.copy()
    
    def save_config(self):
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Config save error: {e}")

system_config = SystemConfiguration()

class SoundManager:
    """Manage system sounds"""
    def __init__(self):
        self.enabled = system_config.config.get("sound", True)
    
    def play_sound(self, sound_type):
        if not self.enabled:
            return

sound_manager = SoundManager()

class WindowManager:
    """Touch-optimized window management"""
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
            window.focus_force()
        except:
            pass
        
        self.animate_window_focus(window)
    
    def lower_window(self, window):
        try:
            window.attributes('-alpha', 0.9)
        except:
            pass
    
    def animate_window_focus(self, window):
        if not system_config.config.get("animations", True):
            window.attributes('-alpha', 1.0)
            return
            
        try:
            steps = [0.7, 0.85, 1.0]
            
            def animate_step(step_index):
                if step_index < len(steps):
                    window.attributes('-alpha', steps[step_index])
                    window.after(30, lambda: animate_step(step_index + 1))
            
            animate_step(0)
        except:
            pass
    
    def close_window(self, window):
        if window in self.windows:
            self.windows.remove(window)
        
        if self.windows:
            self.bring_to_front(self.windows[-1])

window_manager = WindowManager()

class ModernBootScreen:
    """Modern boot screen with enhanced design"""
    def __init__(self, master):
        self.master = master
        self.master.configure(bg='#000010')
        self.master.geometry(f"{MOBILE_WIDTH}x{MOBILE_HEIGHT}")
        self.master.attributes('-alpha', 0.0)
        
        self.boot_frame = tk.Frame(master, bg='#000010')
        self.boot_frame.pack(fill='both', expand=True)
        
        self.animate_boot_start()
        
    def animate_boot_start(self):
        """Animate boot screen appearance"""
        alpha = 0.0
        def fade_in():
            nonlocal alpha
            if alpha < 1.0:
                alpha += 0.05
                self.master.attributes('-alpha', alpha)
                self.master.after(20, fade_in)
            else:
                self.create_boot_interface()
        fade_in()
    
    def create_boot_interface(self):
        # Enhanced animated logo
        self.logo_canvas = tk.Canvas(self.boot_frame, width=250, height=250,
                                    bg='#000010', highlightthickness=0)
        self.logo_canvas.pack(pady=40)
        
        # Enhanced system info
        self.title_label = tk.Label(self.boot_frame, text="QUANTUM OS", 
                                   font=('Arial', 36, 'bold'),
                                   fg='#00ffff', bg='#000010')
        self.title_label.pack(pady=5)
        
        self.subtitle_label = tk.Label(self.boot_frame, text="Premium Mobile Experience",
                                      font=('Arial', 16),
                                      fg='#0088ff', bg='#000010')
        self.subtitle_label.pack(pady=2)
        
        # Modern progress system
        self.progress_container = tk.Frame(self.boot_frame, bg='#000010')
        self.progress_container.pack(pady=30)
        
        self.progress_bg = tk.Frame(self.progress_container, bg='#001122', width=400, height=25)
        self.progress_bg.pack()
        self.progress_bg.pack_propagate(False)
        
        self.progress_fill = tk.Frame(self.progress_bg, bg='#00ffff', height=25, width=0)
        self.progress_fill.pack(side='left', anchor='w')
        
        self.status_label = tk.Label(self.boot_frame, text="",
                                    font=('Arial', 14),
                                    fg='#00ffff', bg='#000010')
        self.status_label.pack(pady=10)
        
        self.boot_time = time.time()
        self.start_boot_sequence()
    
    def draw_enhanced_logo(self, progress):
        """Draw enhanced animated logo"""
        self.logo_canvas.delete('all')
        center_x, center_y = 125, 125
        
        # Enhanced pulsing core
        pulse = 8 * math.sin(time.time() * 2)
        core_size = 30 + (progress / 100) * 40 + pulse
        
        # Glowing outer rings
        for i in range(3):
            radius = 30 + i * 35
            self.logo_canvas.create_oval(
                center_x - radius, center_y - radius,
                center_x + radius, center_y + radius,
                outline='#00ffff', width=2, dash=(8, 4)
            )
        
        # Enhanced main core with gradient effect
        self.logo_canvas.create_oval(
            center_x - core_size, center_y - core_size,
            center_x + core_size, center_y + core_size,
            fill='#00ffff', outline='#0088ff', width=3
        )
        
        # Rotating quantum particles
        particle_count = int(progress / 15) + 4
        for i in range(particle_count):
            angle = time.time() * 3 + i * (2 * math.pi / particle_count)
            radius = 60 + (progress / 100) * 20
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            
            particle_size = 6 + math.sin(time.time() * 5 + i) * 2
            self.logo_canvas.create_oval(
                x-particle_size, y-particle_size, 
                x+particle_size, y+particle_size,
                fill='#ff00ff', outline=''
            )
    
    def start_boot_sequence(self):
        """Start enhanced boot sequence"""
        boot_steps = [
            ("Initializing Quantum Matrix", 10),
            ("Loading Neural Interface", 25),
            ("Starting Core Services", 45),
            ("Optimizing Performance", 65),
            ("Launching Desktop", 85),
            ("System Ready", 100)
        ]
        
        def update_progress(step):
            if step < len(boot_steps):
                text, progress = boot_steps[step]
                self.update_progress_display(progress, text)
                self.master.after(600, lambda: update_progress(step + 1))
            else:
                self.master.after(800, self.complete_boot)
        
        update_progress(0)
    
    def update_progress_display(self, progress, text):
        """Update progress display with smooth animation"""
        progress_width = (progress / 100) * 400
        self.progress_fill.config(width=progress_width)
        self.status_label.config(text=text)
        self.draw_enhanced_logo(progress)
    
    def complete_boot(self):
        """Complete boot process with enhanced transition"""
        self.enhanced_transition()
    
    def enhanced_transition(self):
        """Enhanced transition to desktop"""
        def fade_out():
            current_alpha = 1.0
            def reduce_alpha():
                nonlocal current_alpha
                if current_alpha > 0:
                    current_alpha -= 0.05
                    self.master.attributes('-alpha', current_alpha)
                    self.master.after(20, reduce_alpha)
                else:
                    self.boot_frame.destroy()
                    ModernDesktop(self.master)
            reduce_alpha()
        
        fade_out()

class ModernDesktop:
    """Enhanced modern desktop with better design"""
    def __init__(self, master):
        self.master = master
        self.master.configure(bg='#0a0a20')
        self.master.attributes('-alpha', 0.0)
        
        self.desktop_frame = tk.Frame(master, bg='#0a0a20')
        self.desktop_frame.pack(fill='both', expand=True)
        
        self.setup_enhanced_desktop()
        self.animate_desktop_appear()
    
    def animate_desktop_appear(self):
        """Animate desktop appearance"""
        alpha = 0.0
        def fade_in():
            nonlocal alpha
            if alpha < 1.0:
                alpha += 0.05
                self.master.attributes('-alpha', alpha)
                self.master.after(20, fade_in)
        fade_in()
    
    def setup_enhanced_desktop(self):
        self.create_enhanced_wallpaper()
        self.create_enhanced_taskbar()
        self.create_enhanced_apps()
    
    def create_enhanced_wallpaper(self):
        self.wallpaper_canvas = tk.Canvas(self.desktop_frame, bg='#0a0a20',
                                         highlightthickness=0)
        self.wallpaper_canvas.pack(fill='both', expand=True)
        
        self.draw_enhanced_wallpaper()
    
    def draw_enhanced_wallpaper(self):
        self.wallpaper_canvas.delete('wallpaper')
        width = MOBILE_WIDTH
        height = MOBILE_HEIGHT
        
        # Enhanced animated gradient background
        current_time = time.time()
        for i in range(0, height, 3):
            ratio = i / height
            time_offset = current_time * 0.1
            r = int(10 + math.sin(time_offset + ratio * 2) * 10)
            g = int(20 + math.cos(time_offset + ratio * 3) * 15)
            b = int(40 + math.sin(time_offset + ratio * 4) * 20)
            color = f'#{r:02x}{g:02x}{b:02x}'
            self.wallpaper_canvas.create_line(0, i, width, i, fill=color,
                                            tags='wallpaper')
        
        # Add floating particles with trails
        for i in range(8):
            x = (math.sin(current_time * 0.5 + i) * 0.3 + 0.5) * width
            y = (math.cos(current_time * 0.3 + i) * 0.2 + 0.5) * height
            size = 2 + math.sin(current_time * 2 + i) * 1.5
            color = random.choice(['#00ffff', '#ff00ff', '#ffff00'])
            self.wallpaper_canvas.create_oval(x, y, x+size, y+size, 
                                            fill=color, tags='wallpaper')
        
        # Enhanced clock with better typography
        now = datetime.now()
        time_text = now.strftime("%H:%M:%S")
        date_text = now.strftime("%A, %d %B %Y")
        
        # Clock with shadow effect
        self.wallpaper_canvas.create_text(width//2 + 2, height//2 - 58,
                                         text=time_text,
                                         font=('Arial', 48, 'bold'),
                                         fill='#000033', tags='wallpaper')
        self.wallpaper_canvas.create_text(width//2, height//2 - 60,
                                         text=time_text,
                                         font=('Arial', 48, 'bold'),
                                         fill='#ffffff', tags='wallpaper')
        
        self.wallpaper_canvas.create_text(width//2, height//2,
                                         text=date_text,
                                         font=('Arial', 18),
                                         fill='#8888ff', tags='wallpaper')
        
        user_name = system_config.config.get("user_name", "Quantum User")
        self.wallpaper_canvas.create_text(width//2, height//2 + 50,
                                         text=f"Welcome, {user_name}",
                                         font=('Arial', 14, 'italic'),
                                         fill='#00ffff', tags='wallpaper')
        
        # Update every second for smooth animation
        self.master.after(50, self.draw_enhanced_wallpaper)
    
    def create_enhanced_taskbar(self):
        self.taskbar = tk.Frame(self.master, bg='#1a1a3a', height=80)
        self.taskbar.pack(side='bottom', fill='x')
        self.taskbar.pack_propagate(False)
        
        # Enhanced app launcher
        launcher_frame = tk.Frame(self.taskbar, bg='#1a1a3a')
        launcher_frame.pack(side='left', padx=15, pady=10)
        
        self.app_btn = tk.Button(launcher_frame, text="APPLICATIONS",
                               command=self.show_enhanced_menu,
                               font=('Arial', 14, 'bold'),
                               bg='#00ffff', fg='#000033',
                               relief='flat', padx=20, pady=12)
        TouchOptimizer.make_touch_friendly(self.app_btn)
        self.app_btn.pack()
        
        # Enhanced quick actions
        quick_frame = tk.Frame(self.taskbar, bg='#1a1a3a')
        quick_frame.pack(side='left', padx=20, pady=10)
        
        actions = [
            ("GAMES", self.show_game_hub, "#ff00ff"),
            ("SHOTGUN", self.fire_shotgun, "#ff4444"),
            ("POWER", self.show_power_menu, "#ffff00")
        ]
        
        for text, command, color in actions:
            btn = tk.Button(quick_frame, text=text,
                          command=command,
                          font=('Arial', 11, 'bold'),
                          bg=color, fg='white',
                          width=12, height=2)
            TouchOptimizer.make_touch_friendly(btn)
            btn.pack(side='left', padx=6)
        
        # Enhanced system info panel
        info_frame = tk.Frame(self.taskbar, bg='#1a1a3a')
        info_frame.pack(side='right', padx=20, pady=10)
        
        self.time_label = tk.Label(info_frame, text="",
                                  font=('Arial', 16, 'bold'),
                                  bg='#1a1a3a', fg='#00ffff')
        self.time_label.pack(anchor='e')
        
        battery_level = max(20, 100 - int((time.time() % 120)))
        battery_color = '#00ff00' if battery_level > 50 else '#ffff00' if battery_level > 20 else '#ff4444'
        self.battery_label = tk.Label(info_frame, text=f"BAT {battery_level}%",
                                     font=('Arial', 11),
                                     bg='#1a1a3a', fg=battery_color)
        self.battery_label.pack(anchor='e')
        
        self.update_enhanced_info()
    
    def update_enhanced_info(self):
        now = datetime.now()
        self.time_label.config(text=now.strftime("%H:%M:%S"))
        
        # Enhanced battery simulation
        battery_level = max(20, 100 - int((time.time() % 120)))
        battery_color = '#00ff00' if battery_level > 50 else '#ffff00' if battery_level > 20 else '#ff4444'
        self.battery_label.config(text=f"BAT {battery_level}%", fg=battery_color)
        
        self.master.after(1000, self.update_enhanced_info)
    
    def create_enhanced_apps(self):
        app_container = tk.Frame(self.desktop_frame, bg='', bd=0)
        app_container.place(relx=0.5, rely=0.4, anchor='center')
        
        enhanced_apps = [
            ("EDITOR", self.open_editor, "#00ffff", "Text Editor"),
            ("MUSIC", self.open_media, "#ff00ff", "Media Player"), 
            ("CALC", self.open_calc, "#ffff00", "Calculator"),
            ("BROWSER", self.open_browser, "#00ff88", "Web Browser"),
            ("FILES", self.open_files, "#ff8800", "File Manager"),
            ("SYSTEM", self.open_system, "#8888ff", "System Info"),
            ("SETTINGS", self.open_settings, "#ff0088", "Settings"),
            ("GAMES", self.show_game_hub, "#00ff88", "Game Center")
        ]
        
        for i, (name, command, color, desc) in enumerate(enhanced_apps):
            row = i // 4
            col = i % 4
            
            app = self.create_enhanced_app(app_container, name, color, command, desc)
            app.grid(row=row, column=col, padx=12, pady=12)
    
    def create_enhanced_app(self, parent, name, color, command, description):
        frame = tk.Frame(parent, bg='#1a1a3a', width=120, height=140,
                        relief='flat', bd=2, highlightbackground=color,
                        highlightthickness=2)
        frame.pack_propagate(False)
        
        # Enhanced app icon with gradient effect
        icon_canvas = tk.Canvas(frame, bg=color, width=70, height=70, 
                               highlightthickness=0)
        icon_canvas.place(relx=0.5, rely=0.35, anchor='center')
        
        # Draw simple icon representation
        icon_canvas.create_oval(10, 10, 60, 60, fill=self.lighten_color(color), outline='')
        icon_canvas.create_oval(15, 15, 55, 55, fill=color, outline='')
        
        # App name with better styling
        name_label = tk.Label(frame, text=name,
                             font=('Arial', 10, 'bold'),
                             bg='#1a1a3a', fg='white',
                             wraplength=100)
        name_label.place(relx=0.5, rely=0.7, anchor='center')
        
        # App description
        desc_label = tk.Label(frame, text=description,
                             font=('Arial', 8),
                             bg='#2a2a4a', fg='#aaaaaa')
        desc_label.place(relx=0.5, rely=0.85, anchor='center')
        
        # Enhanced touch events with visual feedback
        def on_touch(event):
            sound_manager.play_sound("click")
            frame.configure(bg='#2a2a4a', highlightbackground=self.lighten_color(color))
            icon_canvas.configure(bg=self.lighten_color(color))
        
        def on_release(event):
            frame.configure(bg='#1a1a3a', highlightbackground=color)
            icon_canvas.configure(bg=color)
            frame.after(100, command)
        
        for child in [frame, name_label, desc_label, icon_canvas]:
            child.bind('<ButtonPress-1>', on_touch)
            child.bind('<ButtonRelease-1>', on_release)
        
        return frame
    
    def lighten_color(self, color):
        """Lighten color for hover effect"""
        r = min(255, int(color[1:3], 16) + 40)
        g = min(255, int(color[3:5], 16) + 40)
        b = min(255, int(color[5:7], 16) + 40)
        return f'#{r:02x}{g:02x}{b:02x}'
    
    def show_enhanced_menu(self):
        EnhancedAppMenu(self.master)
    
    def show_power_menu(self):
        EnhancedPowerMenu(self.master)
    
    def show_game_hub(self):
        EnhancedGameHub(self.master)
    
    def fire_shotgun(self):
        EnhancedShotgunEffect(self.master)
    
    def open_editor(self):
        EnhancedTextEditor(self.master)
    
    def open_media(self):
        EnhancedMediaPlayer(self.master)
    
    def open_calc(self):
        EnhancedCalculator(self.master)
    
    def open_browser(self):
        EnhancedWebBrowser(self.master)
    
    def open_files(self):
        EnhancedFileManager(self.master)
    
    def open_system(self):
        EnhancedSystemInfo(self.master)
    
    def open_settings(self):
        EnhancedSettings(self.master)

class EnhancedAppMenu:
    """Enhanced app menu with better design"""
    def __init__(self, master):
        self.master = master
        self.create_enhanced_menu()
    
    def create_enhanced_menu(self):
        self.menu = tk.Toplevel(self.master)
        self.menu.configure(bg='#1a1a3a')
        self.menu.overrideredirect(True)
        
        menu_width = MOBILE_WIDTH - 80
        menu_height = 500
        x = (MOBILE_WIDTH - menu_width) // 2
        y = MOBILE_HEIGHT - menu_height - 80
        
        self.menu.geometry(f"{menu_width}x{menu_height}+{x}+{y}")
        self.menu.attributes('-alpha', 0.0)
        
        self.build_enhanced_menu()
        self.enhanced_animate_open()
        
        # Close when clicking outside
        self.menu.bind('<FocusOut>', lambda e: self.enhanced_animate_close())
    
    def build_enhanced_menu(self):
        # Enhanced header with gradient
        header = tk.Frame(self.menu, bg='#00ffff', height=70)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        tk.Label(header, text="APPLICATION LAUNCHER",
                font=('Arial', 20, 'bold'),
                bg='#00ffff', fg='#000033').pack(pady=20)
        
        # Enhanced app grid with scroll
        container = tk.Frame(self.menu, bg='#1a1a3a')
        container.pack(fill='both', expand=True, padx=25, pady=20)
        
        # Create scrollable frame
        canvas = tk.Canvas(container, bg='#1a1a3a', highlightthickness=0)
        scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='#1a1a3a')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        apps = [
            ("Text Editor", "Create and edit documents", self.open_editor),
            ("Media Player", "Play music and audio", self.open_media),
            ("Calculator", "Scientific calculator", self.open_calc),
            ("Web Browser", "Browse the internet", self.open_browser),
            ("File Manager", "Manage your files", self.open_files),
            ("System Info", "System information", self.open_system),
            ("Settings", "System settings", self.open_settings),
            ("Space Shooter", "Arcade space game", self.open_shooter),
            ("Quantum Runner", "Endless runner game", self.open_runner),
            ("Puzzle Challenge", "Slide puzzle game", self.open_puzzle),
            ("Memory Cards", "Memory matching game", self.open_memory),
            ("Power Options", "Shutdown and restart", self.open_power)
        ]
        
        for name, desc, command in apps:
            btn_frame = tk.Frame(scrollable_frame, bg='#2a2a4a', relief='flat', bd=1)
            btn_frame.pack(fill='x', pady=6)
            
            btn = tk.Button(btn_frame, text=name, font=('Arial', 13),
                          bg='#2a2a4a', fg='white', width=28,
                          command=command, anchor='w', justify='left')
            btn.pack(side='left', padx=15, pady=10)
            
            desc_label = tk.Label(btn_frame, text=desc, font=('Arial', 10),
                                bg='#2a2a4a', fg='#8888ff')
            desc_label.pack(side='right', padx=15)
            
            TouchOptimizer.make_touch_friendly(btn)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
    def enhanced_animate_open(self):
        alpha = 0.0
        def fade_in():
            nonlocal alpha
            if alpha < 0.95:
                alpha += 0.1
                self.menu.attributes('-alpha', alpha)
                self.menu.after(15, fade_in)
            else:
                self.menu.focus_force()
        fade_in()
    
    def enhanced_animate_close(self):
        alpha = 0.95
        def fade_out():
            nonlocal alpha
            if alpha > 0:
                alpha -= 0.1
                self.menu.attributes('-alpha', alpha)
                self.menu.after(15, fade_out)
            else:
                self.menu.destroy()
        fade_out()
    
    def open_editor(self):
        EnhancedTextEditor(self.master)
        self.enhanced_animate_close()
    
    def open_media(self):
        EnhancedMediaPlayer(self.master)
        self.enhanced_animate_close()
    
    def open_calc(self):
        EnhancedCalculator(self.master)
        self.enhanced_animate_close()
    
    def open_browser(self):
        EnhancedWebBrowser(self.master)
        self.enhanced_animate_close()
    
    def open_files(self):
        EnhancedFileManager(self.master)
        self.enhanced_animate_close()
    
    def open_system(self):
        EnhancedSystemInfo(self.master)
        self.enhanced_animate_close()
    
    def open_settings(self):
        EnhancedSettings(self.master)
        self.enhanced_animate_close()
    
    def open_shooter(self):
        SpaceShooterGame(self.master)
        self.enhanced_animate_close()
    
    def open_runner(self):
        QuantumRunnerGame(self.master)
        self.enhanced_animate_close()
    
    def open_puzzle(self):
        PuzzleGame(self.master)
        self.enhanced_animate_close()
    
    def open_memory(self):
        MemoryCardGame(self.master)
        self.enhanced_animate_close()
    
    def open_power(self):
        self.enhanced_animate_close()
        EnhancedPowerMenu(self.master)

class EnhancedPowerMenu:
    """Enhanced power menu with better animations"""
    def __init__(self, master):
        self.master = master
        self.create_enhanced_power_menu()
    
    def create_enhanced_power_menu(self):
        self.power_menu = tk.Toplevel(self.master)
        self.power_menu.configure(bg='#1a1a1a')
        self.power_menu.overrideredirect(True)
        
        width, height = 350, 400
        x = (MOBILE_WIDTH - width) // 2
        y = (MOBILE_HEIGHT - height) // 2
        
        self.power_menu.geometry(f"{width}x{height}+{x}+{y}")
        self.power_menu.attributes('-alpha', 0.0)
        
        self.build_enhanced_power_interface()
        self.enhanced_animate_open()
    
    def build_enhanced_power_interface(self):
        # Enhanced header
        header = tk.Frame(self.power_menu, bg='#ff4444', height=80)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        tk.Label(header, text="POWER OPTIONS",
                font=('Arial', 20, 'bold'),
                bg='#ff4444', fg='white').pack(pady=25)
        
        # Enhanced power options
        options_frame = tk.Frame(self.power_menu, bg='#1a1a1a')
        options_frame.pack(fill='both', expand=True, padx=25, pady=25)
        
        power_options = [
            ("SHUTDOWN", "Turn off the system", self.shutdown_system, "#ff4444"),
            ("RESTART", "Restart the system", self.restart_system, "#ff8800"), 
            ("SLEEP", "Put to sleep", self.sleep_system, "#0088ff"),
            ("LOCK", "Lock system", self.lock_system, "#00ff88"),
            ("CANCEL", "Return to system", self.cancel, "#666666")
        ]
        
        for text, desc, command, color in power_options:
            btn_frame = tk.Frame(options_frame, bg='#2a2a2a')
            btn_frame.pack(fill='x', pady=4)
            
            btn = tk.Button(btn_frame, text=f"{text}\n{desc}",
                          command=command,
                          font=('Arial', 12, 'bold'),
                          bg=color, fg='white',
                          width=30, height=3,
                          justify='center')
            TouchOptimizer.make_touch_friendly(btn)
            btn.pack(fill='x', padx=2, pady=2)
    
    def enhanced_animate_open(self):
        alpha = 0.0
        def fade_in():
            nonlocal alpha
            if alpha < 1.0:
                alpha += 0.1
                self.power_menu.attributes('-alpha', alpha)
                self.power_menu.after(20, fade_in)
        fade_in()
    
    def shutdown_system(self):
        self.enhanced_animate_close()
        EnhancedShutdownSequence(self.master)
    
    def restart_system(self):
        messagebox.showinfo("Restart", "System restart initiated!")
        self.enhanced_animate_close()
    
    def sleep_system(self):
        messagebox.showinfo("Sleep", "System going to sleep!")
        self.enhanced_animate_close()
    
    def lock_system(self):
        messagebox.showinfo("Lock", "System locked!")
        self.enhanced_animate_close()
    
    def cancel(self):
        self.enhanced_animate_close()
    
    def enhanced_animate_close(self):
        alpha = 1.0
        def fade_out():
            nonlocal alpha
            if alpha > 0:
                alpha -= 0.1
                self.power_menu.attributes('-alpha', alpha)
                self.power_menu.after(20, fade_out)
            else:
                self.power_menu.destroy()
        fade_out()

class EnhancedWindow:
    """Enhanced window base class with better design"""
    def __init__(self, master, title, width=None, height=None):
        if width is None:
            width = min(MOBILE_WIDTH - 50, 650)
        if height is None:
            height = min(MOBILE_HEIGHT - 100, 550)
            
        self.window = tk.Toplevel(master)
        self.window.title(title)
        self.window.configure(bg='#1a1a3a')
        self.window.attributes('-alpha', 0.0)
        
        x = (MOBILE_WIDTH - width) // 2
        y = (MOBILE_HEIGHT - height) // 2
        self.window.geometry(f"{width}x{height}+{x}+{y}")
        
        self.create_enhanced_interface(title)
        window_manager.add_window(self.window)
        
        self.enhanced_animate_open()
    
    def create_enhanced_interface(self, title):
        # Enhanced title bar with gradient
        self.title_bar = tk.Frame(self.window, bg='#00ffff', height=50)
        self.title_bar.pack(fill='x')
        self.title_bar.pack_propagate(False)
        
        tk.Label(self.title_bar, text=title,
                font=('Arial', 15, 'bold'),
                bg='#00ffff', fg='#000033').pack(side='left', padx=20, pady=15)
        
        # Enhanced controls
        controls = tk.Frame(self.title_bar, bg='#00ffff')
        controls.pack(side='right', padx=10)
        
        close_btn = tk.Button(controls, text="X",
                 command=self.enhanced_animate_close,
                 font=('Arial', 14, 'bold'),
                 bg='#ff4444', fg='white',
                 width=3, height=1)
        TouchOptimizer.make_touch_friendly(close_btn)
        close_btn.pack(side='left', padx=2)
        
        # Enhanced content area
        self.content = tk.Frame(self.window, bg='#1a1a3a')
        self.content.pack(fill='both', expand=True, padx=2, pady=2)
    
    def enhanced_animate_open(self):
        alpha = 0.0
        def fade_in():
            nonlocal alpha
            if alpha < 1.0:
                alpha += 0.1
                self.window.attributes('-alpha', alpha)
                self.window.after(20, fade_in)
        fade_in()
    
    def enhanced_animate_close(self):
        sound_manager.play_sound("click")
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

# Enhanced Applications
class EnhancedTextEditor(EnhancedWindow):
    def __init__(self, master):
        super().__init__(master, "Enhanced Text Editor", 700, 500)
        self.setup_editor()
    
    def setup_editor(self):
        # Enhanced toolbar
        toolbar = tk.Frame(self.content, bg='#2a2a4a', height=50)
        toolbar.pack(fill='x', padx=10, pady=8)
        toolbar.pack_propagate(False)
        
        buttons = [
            ("New", self.new_file),
            ("Open", self.open_file),
            ("Save", self.save_file),
            ("Format", self.format_text),
            ("Find", self.find_text)
        ]
        
        for text, command in buttons:
            btn = tk.Button(toolbar, text=text, command=command,
                          font=('Arial', 11), bg='#00ffff', fg='#000033')
            TouchOptimizer.make_touch_friendly(btn)
            btn.pack(side='left', padx=8, pady=6)
        
        # Enhanced text area with line numbers
        text_frame = tk.Frame(self.content, bg='#1a1a3a')
        text_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Line numbers
        self.line_numbers = tk.Text(text_frame, width=4, padx=5, pady=5,
                                   bg='#2a2a4a', fg='#8888ff', 
                                   font=('Arial', 12), state='disabled')
        self.line_numbers.pack(side='left', fill='y')
        
        # Main text area
        self.text_area = scrolledtext.ScrolledText(text_frame,
                                                  font=('Arial', 13),
                                                  bg='#0a0a2a', fg='#ffffff',
                                                  insertbackground='#00ffff',
                                                  padx=10, pady=10,
                                                  wrap=tk.WORD,
                                                  selectbackground='#ff00ff',
                                                  undo=True)
        self.text_area.pack(side='left', fill='both', expand=True)
        
        # Bind events for line numbers
        self.text_area.bind('<KeyRelease>', self.update_line_numbers)
        self.text_area.bind('<MouseWheel>', self.update_line_numbers)
        
        # Enhanced status bar
        self.status = tk.Label(self.content, text="Ready - New Document",
                              font=('Arial', 10),
                              bg='#2a2a4a', fg='#8888ff',
                              anchor='w')
        self.status.pack(fill='x', side='bottom')
        
        self.current_file = None
        self.text_area.focus()
        self.update_line_numbers()
    
    def update_line_numbers(self, event=None):
        lines = self.text_area.get('1.0', 'end-1c').split('\n')
        line_numbers_text = '\n'.join(str(i) for i in range(1, len(lines) + 1))
        
        self.line_numbers.config(state='normal')
        self.line_numbers.delete('1.0', 'end')
        self.line_numbers.insert('1.0', line_numbers_text)
        self.line_numbers.config(state='disabled')
    
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.current_file = None
        self.status.config(text="New document created")
        self.update_line_numbers()
    
    def save_file(self):
        try:
            content = self.text_area.get(1.0, tk.END)
            filename = filedialog.asksaveasfilename(
                defaultextension=".txt",
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            if filename:
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(content)
                self.current_file = filename
                self.status.config(text=f"Document saved: {os.path.basename(filename)}")
                messagebox.showinfo("Success", "Document saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Save failed: {str(e)}")
    
    def open_file(self):
        try:
            filename = filedialog.askopenfilename(
                filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
            )
            if filename:
                with open(filename, "r", encoding="utf-8") as f:
                    content = f.read()
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(1.0, content)
                self.current_file = filename
                self.status.config(text=f"Document loaded: {os.path.basename(filename)}")
                self.update_line_numbers()
        except Exception as e:
            messagebox.showerror("Error", f"Open failed: {str(e)}")
    
    def format_text(self):
        messagebox.showinfo("Format", "Text formatting applied!")
        self.status.config(text="Text formatted")
    
    def find_text(self):
        find_window = tk.Toplevel(self.window)
        find_window.title("Find Text")
        find_window.geometry("300x150")
        find_window.configure(bg='#2a2a4a')
        
        tk.Label(find_window, text="Find:", bg='#2a2a4a', fg='white').pack(pady=10)
        find_entry = tk.Entry(find_window, width=30, font=('Arial', 12))
        find_entry.pack(pady=5)
        
        def find():
            text_to_find = find_entry.get()
            if text_to_find:
                content = self.text_area.get(1.0, tk.END)
                if text_to_find in content:
                    self.text_area.tag_remove('found', 1.0, tk.END)
                    start = '1.0'
                    while True:
                        start = self.text_area.search(text_to_find, start, tk.END)
                        if not start:
                            break
                        end = f"{start}+{len(text_to_find)}c"
                        self.text_area.tag_add('found', start, end)
                        start = end
                    self.text_area.tag_config('found', background='#ff00ff')
                    find_window.destroy()
                else:
                    messagebox.showinfo("Find", "Text not found!")
        
        tk.Button(find_window, text="Find", command=find, bg='#00ffff').pack(pady=10)

class EnhancedMediaPlayer(EnhancedWindow):
    def __init__(self, master):
        super().__init__(master, "Media Player", 500, 400)
        self.setup_player()
    
    def setup_player(self):
        # Header
        header = tk.Label(self.content, text="Quantum Media Player",
                         font=('Arial', 18, 'bold'),
                         bg='#1a1a3a', fg='#ff00ff')
        header.pack(pady=20)
        
        # Playlist
        playlist_frame = tk.Frame(self.content, bg='#2a2a4a')
        playlist_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        tk.Label(playlist_frame, text="Playlist:", 
                font=('Arial', 12, 'bold'),
                bg='#2a2a4a', fg='white').pack(anchor='w')
        
        playlist_list = tk.Listbox(playlist_frame, bg='#0a0a2a', fg='white',
                                 font=('Arial', 11), height=8)
        playlist_list.pack(fill='both', expand=True, pady=10)
        
        # Add sample songs
        sample_songs = [
            "Quantum Waves - Ambient Mix",
            "Neon Dreams - Synthwave", 
            "Cosmic Journey - Space Music",
            "Digital Rain - Chillout",
            "Future Memories - Electronic"
        ]
        
        for song in sample_songs:
            playlist_list.insert(tk.END, song)
        
        # Controls
        controls_frame = tk.Frame(self.content, bg='#1a1a3a')
        controls_frame.pack(fill='x', padx=20, pady=15)
        
        control_buttons = [
            ("<<", lambda: self.show_message("Previous")),
            ("Play", lambda: self.show_message("Play/Pause")),
            (">>", lambda: self.show_message("Next")),
            ("Shuffle", lambda: self.show_message("Shuffle")),
            ("Repeat", lambda: self.show_message("Repeat"))
        ]
        
        for text, command in control_buttons:
            btn = tk.Button(controls_frame, text=text, command=command,
                          font=('Arial', 12), bg='#ff00ff', fg='white',
                          width=8)
            TouchOptimizer.make_touch_friendly(btn)
            btn.pack(side='left', padx=8)
        
        # Volume slider
        volume_frame = tk.Frame(self.content, bg='#1a1a3a')
        volume_frame.pack(fill='x', padx=20, pady=10)
        
        tk.Label(volume_frame, text="Volume:", bg='#1a1a3a', fg='white').pack(side='left')
        volume_scale = tk.Scale(volume_frame, from_=0, to=100, orient='horizontal',
                              bg='#1a1a3a', fg='white', highlightbackground='#1a1a3a')
        volume_scale.set(75)
        volume_scale.pack(side='left', fill='x', expand=True, padx=10)
    
    def show_message(self, action):
        messagebox.showinfo("Media Player", f"{action} clicked!\n(Audio functionality would be implemented here)")

class EnhancedCalculator(EnhancedWindow):
    def __init__(self, master):
        super().__init__(master, "Calculator", 350, 450)
        self.setup_calculator()
    
    def setup_calculator(self):
        self.result_var = tk.StringVar(value="0")
        self.current_input = ""
        self.operator = ""
        self.previous_value = 0
        
        # Display
        display_frame = tk.Frame(self.content, bg='#2a2a4a')
        display_frame.pack(fill='x', padx=15, pady=15)
        
        display = tk.Entry(display_frame, textvariable=self.result_var,
                          font=('Arial', 20), justify='right',
                          bg='#0a0a2a', fg='#00ffff', bd=0,
                          state='readonly')
        display.pack(fill='x', ipady=10)
        
        # Button grid
        button_frame = tk.Frame(self.content, bg='#1a1a3a')
        button_frame.pack(fill='both', expand=True, padx=15, pady=10)
        
        buttons = [
            ('C', '+/-', '%', '/'),
            ('7', '8', '9', '*'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('0', '', '.', '=')
        ]
        
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                if text:
                    btn = tk.Button(button_frame, text=text,
                                  font=('Arial', 16),
                                  command=lambda t=text: self.button_click(t),
                                  bg=self.get_button_color(text),
                                  fg='white',
                                  relief='flat',
                                  height=2, width=5)
                    btn.grid(row=i, column=j, padx=2, pady=2, sticky='nsew')
                    
                    if text == '0':
                        btn.grid(columnspan=2, sticky='nsew')
        
        # Configure grid weights
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.grid_columnconfigure(j, weight=1)
    
    def get_button_color(self, text):
        if text in ['/', '*', '-', '+', '=']:
            return '#ff00ff'
        elif text in ['C', '+/-', '%']:
            return '#00ffff'
        else:
            return '#2a2a4a'
    
    def button_click(self, text):
        if text.isdigit() or text == '.':
            if self.current_input == "0" or self.operator == "=":
                self.current_input = text
            else:
                self.current_input += text
            self.result_var.set(self.current_input)
        
        elif text in ['+', '-', '*', '/']:
            if self.current_input:
                self.previous_value = float(self.current_input)
            self.operator = text
            self.current_input = ""
        
        elif text == '=':
            if self.operator and self.current_input:
                current_value = float(self.current_input)
                if self.operator == '+':
                    result = self.previous_value + current_value
                elif self.operator == '-':
                    result = self.previous_value - current_value
                elif self.operator == '*':
                    result = self.previous_value * current_value
                elif self.operator == '/':
                    result = self.previous_value / current_value if current_value != 0 else "Error"
                
                self.result_var.set(str(result))
                self.current_input = str(result)
                self.operator = "="
        
        elif text == 'C':
            self.current_input = ""
            self.operator = ""
            self.previous_value = 0
            self.result_var.set("0")
        
        elif text == '+/-':
            if self.current_input:
                self.current_input = str(-float(self.current_input))
                self.result_var.set(self.current_input)
        
        elif text == '%':
            if self.current_input:
                self.current_input = str(float(self.current_input) / 100)
                self.result_var.set(self.current_input)

class EnhancedWebBrowser(EnhancedWindow):
    def __init__(self, master):
        super().__init__(master, "Web Browser", 600, 500)
        self.setup_browser()
    
    def setup_browser(self):
        # Navigation bar
        nav_frame = tk.Frame(self.content, bg='#2a2a4a', height=50)
        nav_frame.pack(fill='x', padx=10, pady=10)
        nav_frame.pack_propagate(False)
        
        self.url_var = tk.StringVar(value="https://www.example.com")
        url_entry = tk.Entry(nav_frame, textvariable=self.url_var,
                           font=('Arial', 12), bg='#0a0a2a', fg='white')
        url_entry.pack(side='left', fill='x', expand=True, padx=5, pady=10)
        
        nav_buttons = [
            ("Back", self.go_back),
            ("Forward", self.go_forward),
            ("Refresh", self.refresh),
            ("Go", self.browse)
        ]
        
        for text, command in nav_buttons:
            btn = tk.Button(nav_frame, text=text, command=command,
                          font=('Arial', 11), bg='#00ffff', fg='#000033')
            btn.pack(side='left', padx=2, pady=10)
        
        # Browser content
        content_frame = tk.Frame(self.content, bg='#1a1a3a')
        content_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        browser_text = scrolledtext.ScrolledText(content_frame,
                                               font=('Arial', 11),
                                               bg='white', fg='black',
                                               wrap=tk.WORD)
        browser_text.pack(fill='both', expand=True)
        
        # Sample browser content
        sample_content = """QUANTUM WEB BROWSER

Welcome to Quantum Browser!

This is a simulated web browser interface. In a real implementation, this would display actual web pages.

Features:
• Fast browsing experience
• Secure connections
• Tabbed browsing
• Bookmark management

Try navigating to:
• https://www.example.com
• https://www.quantum-os.com
• https://www.sample-site.org

Note: This is a demonstration interface. Actual web browsing functionality would require integration with a web rendering engine.
"""
        browser_text.insert('1.0', sample_content)
        browser_text.config(state='disabled')
    
    def go_back(self):
        messagebox.showinfo("Browser", "Back button clicked")
    
    def go_forward(self):
        messagebox.showinfo("Browser", "Forward button clicked")
    
    def refresh(self):
        messagebox.showinfo("Browser", "Page refreshed")
    
    def browse(self):
        url = self.url_var.get()
        messagebox.showinfo("Browser", f"Navigating to: {url}\n\n(In real implementation, this would load the webpage)")

class EnhancedFileManager(EnhancedWindow):
    def __init__(self, master):
        super().__init__(master, "File Manager", 550, 450)
        self.setup_file_manager()
    
    def setup_file_manager(self):
        # Toolbar
        toolbar = tk.Frame(self.content, bg='#2a2a4a', height=40)
        toolbar.pack(fill='x', padx=10, pady=10)
        toolbar.pack_propagate(False)
        
        tools = [
            ("New Folder", self.new_folder),
            ("New File", self.new_file),
            ("Delete", self.delete_file),
            ("Copy", self.copy_file),
            ("Cut", self.cut_file),
            ("Paste", self.paste_file)
        ]
        
        for text, command in tools:
            btn = tk.Button(toolbar, text=text, command=command,
                          font=('Arial', 10), bg='#00ffff', fg='#000033')
            btn.pack(side='left', padx=5, pady=5)
        
        # File list
        list_frame = tk.Frame(self.content, bg='#1a1a3a')
        list_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Treeview for files
        columns = ('name', 'size', 'type', 'modified')
        self.tree = ttk.Treeview(list_frame, columns=columns, show='tree headings')
        
        self.tree.heading('name', text='Name')
        self.tree.heading('size', text='Size')
        self.tree.heading('type', text='Type')
        self.tree.heading('modified', text='Modified')
        
        self.tree.column('name', width=200)
        self.tree.column('size', width=80)
        self.tree.column('type', width=100)
        self.tree.column('modified', width=120)
        
        # Sample files
        sample_files = [
            ('document.txt', '1.2 KB', 'Text File', '2024-01-15 10:30'),
            ('image.png', '2.3 MB', 'Image', '2024-01-14 15:45'),
            ('music.mp3', '4.5 MB', 'Audio', '2024-01-13 09:20'),
            ('data.xlsx', '356 KB', 'Spreadsheet', '2024-01-12 14:15'),
            ('script.py', '15 KB', 'Python File', '2024-01-11 11:00')
        ]
        
        for file in sample_files:
            self.tree.insert('', 'end', values=file)
        
        scrollbar = ttk.Scrollbar(list_frame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Status bar
        status = tk.Label(self.content, text="5 items", 
                         font=('Arial', 10),
                         bg='#2a2a4a', fg='#8888ff')
        status.pack(fill='x', side='bottom')
    
    def new_folder(self):
        name = simpledialog.askstring("New Folder", "Enter folder name:")
        if name:
            messagebox.showinfo("File Manager", f"Created folder: {name}")
    
    def new_file(self):
        name = simpledialog.askstring("New File", "Enter file name:")
        if name:
            messagebox.showinfo("File Manager", f"Created file: {name}")
    
    def delete_file(self):
        messagebox.showinfo("File Manager", "Delete file clicked")
    
    def copy_file(self):
        messagebox.showinfo("File Manager", "Copy file clicked")
    
    def cut_file(self):
        messagebox.showinfo("File Manager", "Cut file clicked")
    
    def paste_file(self):
        messagebox.showinfo("File Manager", "Paste file clicked")

class EnhancedSystemInfo(EnhancedWindow):
    def __init__(self, master):
        super().__init__(master, "System Information", 500, 400)
        self.setup_system_info()
    
    def setup_system_info(self):
        # System overview
        overview_frame = tk.Frame(self.content, bg='#2a2a4a')
        overview_frame.pack(fill='x', padx=20, pady=20)
        
        tk.Label(overview_frame, text="QUANTUM OS - SYSTEM OVERVIEW",
                font=('Arial', 16, 'bold'),
                bg='#2a2a4a', fg='#00ffff').pack(pady=10)
        
        # System details
        details = [
            ("OS Version:", "Quantum OS v2.1.0"),
            ("Build Number:", "QOS-2024.01.15"),
            ("System Uptime:", "2 hours, 15 minutes"),
            ("Memory Usage:", "1.2 GB / 4.0 GB (30%)"),
            ("Storage:", "45 GB / 128 GB (35%)"),
            ("Battery:", "78% - Charging"),
            ("Network:", "WiFi Connected - Quantum_Network"),
            ("Last Update:", "2024-01-15 08:30")
        ]
        
        for label, value in details:
            detail_frame = tk.Frame(self.content, bg='#1a1a3a')
            detail_frame.pack(fill='x', padx=30, pady=3)
            
            tk.Label(detail_frame, text=label, font=('Arial', 11, 'bold'),
                    bg='#1a1a3a', fg='#00ffff', width=15, anchor='w').pack(side='left')
            tk.Label(detail_frame, text=value, font=('Arial', 11),
                    bg='#1a1a3a', fg='white', anchor='w').pack(side='left', fill='x', expand=True)
        
        # Performance metrics
        metrics_frame = tk.Frame(self.content, bg='#2a2a4a')
        metrics_frame.pack(fill='x', padx=20, pady=15)
        
        tk.Label(metrics_frame, text="Performance Metrics",
                font=('Arial', 14, 'bold'),
                bg='#2a2a4a', fg='#ff00ff').pack()
        
        # CPU usage bar
        cpu_frame = tk.Frame(self.content, bg='#1a1a3a')
        cpu_frame.pack(fill='x', padx=30, pady=8)
        
        tk.Label(cpu_frame, text="CPU Usage: 45%", 
                bg='#1a1a3a', fg='white').pack(anchor='w')
        cpu_bar = tk.Frame(cpu_frame, bg='#00ff00', height=10, width=180)
        cpu_bar.pack(anchor='w', pady=2)
        
        # Memory usage bar
        mem_frame = tk.Frame(self.content, bg='#1a1a3a')
        mem_frame.pack(fill='x', padx=30, pady=8)
        
        tk.Label(mem_frame, text="Memory Usage: 30%", 
                bg='#1a1a3a', fg='white').pack(anchor='w')
        mem_bar = tk.Frame(mem_frame, bg='#ff00ff', height=10, width=120)
        mem_bar.pack(anchor='w', pady=2)

class EnhancedSettings(EnhancedWindow):
    def __init__(self, master):
        super().__init__(master, "System Settings", 500, 500)
        self.setup_settings()
    
    def setup_settings(self):
        # Settings categories
        categories = [
            ("Appearance", self.appearance_settings),
            ("Sound", self.sound_settings),
            ("Security", self.security_settings),
            ("Network", self.network_settings),
            ("Display", self.display_settings),
            ("Performance", self.performance_settings)
        ]
        
        for i, (name, command) in enumerate(categories):
            btn = tk.Button(self.content, text=name, command=command,
                          font=('Arial', 12), bg='#2a2a4a', fg='white',
                          width=30, height=2, anchor='w')
            btn.pack(pady=8, padx=50, fill='x')
            TouchOptimizer.make_touch_friendly(btn)
    
    def appearance_settings(self):
        self.show_settings_panel("Appearance", [
            ("Theme", ["Quantum Dark", "Quantum Light", "Blue Ocean", "Sunset"]),
            ("Wallpaper", ["Dynamic", "Stars", "Gradient", "Solid Color"]),
            ("Font Size", ["Small", "Medium", "Large", "X-Large"]),
            ("Animations", ["Enabled", "Disabled"])
        ])
    
    def sound_settings(self):
        self.show_settings_panel("Sound", [
            ("System Sounds", ["Enabled", "Disabled"]),
            ("Volume", ["0%", "25%", "50%", "75%", "100%"]),
            ("Notification Sound", ["Chime", "Beep", "Wave", "Silent"]),
            ("Media Volume", ["0%", "25%", "50%", "75%", "100%"])
        ])
    
    def security_settings(self):
        self.show_settings_panel("Security", [
            ("Screen Lock", ["Enabled", "Disabled"]),
            ("Auto-Lock", ["1 minute", "5 minutes", "15 minutes", "Never"]),
            ("App Permissions", ["Manage"]),
            ("Privacy", ["Enhanced", "Standard", "Minimal"])
        ])
    
    def network_settings(self):
        self.show_settings_panel("Network", [
            ("WiFi", ["Quantum_Network", "Search Networks..."]),
            ("Bluetooth", ["Enabled", "Disabled"]),
            ("Mobile Data", ["Enabled", "Disabled"]),
            ("VPN", ["Not Configured", "Setup VPN"])
        ])
    
    def display_settings(self):
        self.show_settings_panel("Display", [
            ("Brightness", ["Auto", "25%", "50%", "75%", "100%"]),
            ("Timeout", ["30 seconds", "1 minute", "5 minutes", "Never"]),
            ("Night Light", ["Enabled", "Disabled"]),
            ("Display Size", ["Small", "Medium", "Large"])
        ])
    
    def performance_settings(self):
        self.show_settings_panel("Performance", [
            ("Power Mode", ["Balanced", "Power Saver", "High Performance"]),
            ("Background Apps", ["Restricted", "Optimized", "Unrestricted"]),
            ("Storage Cleanup", ["Run Cleanup"]),
            ("Developer Options", ["Disabled", "Enabled"])
        ])
    
    def show_settings_panel(self, title, settings):
        panel = tk.Toplevel(self.window)
        panel.title(f"{title} Settings")
        panel.geometry("400x400")
        panel.configure(bg='#1a1a3a')
        
        tk.Label(panel, text=title, font=('Arial', 18, 'bold'),
                bg='#1a1a3a', fg='#00ffff').pack(pady=20)
        
        for setting_name, options in settings:
            frame = tk.Frame(panel, bg='#1a1a3a')
            frame.pack(fill='x', padx=30, pady=10)
            
            tk.Label(frame, text=setting_name, font=('Arial', 11, 'bold'),
                    bg='#1a1a3a', fg='white').pack(anchor='w')
            
            var = tk.StringVar(value=options[0])
            dropdown = ttk.Combobox(frame, textvariable=var, values=options,
                                  state='readonly', font=('Arial', 10))
            dropdown.pack(fill='x', pady=5)
        
        tk.Button(panel, text="Apply Settings", 
                 command=lambda: messagebox.showinfo("Settings", "Settings applied successfully!"),
                 bg='#00ffff', fg='#000033', font=('Arial', 12)).pack(pady=20)

# Enhanced Game Hub
class EnhancedGameHub(EnhancedWindow):
    """Enhanced Game Hub with all games working"""
    def __init__(self, master):
        super().__init__(master, "Game Hub", 450, 550)
        self.setup_game_hub()
    
    def setup_game_hub(self):
        header = tk.Label(self.content, text="GAME COLLECTION",
                         font=('Arial', 22, 'bold'),
                         bg='#1a1a3a', fg='#00ffff')
        header.pack(pady=25)
        
        games = [
            ("Space Shooter", "Arcade space combat", SpaceShooterGame),
            ("Quantum Runner", "Endless runner game", QuantumRunnerGame),
            ("Puzzle Challenge", "Slide puzzle game", PuzzleGame),
            ("Memory Cards", "Memory matching game", MemoryCardGame)
        ]
        
        for name, desc, game_class in games:
            game_frame = tk.Frame(self.content, bg='#2a2a4a', relief='flat', bd=2)
            game_frame.pack(fill='x', padx=35, pady=15)
            
            tk.Label(game_frame, text=name, font=('Arial', 16, 'bold'),
                    bg='#2a2a4a', fg='#00ffff').pack(pady=8)
            
            tk.Label(game_frame, text=desc, font=('Arial', 11),
                    bg='#2a2a4a', fg='#8888ff').pack(pady=4)
            
            play_btn = tk.Button(game_frame, text="PLAY", 
                               command=lambda gc=game_class: gc(self.window),
                               bg='#ff00ff', fg='white', font=('Arial', 12, 'bold'))
            TouchOptimizer.make_touch_friendly(play_btn)
            play_btn.pack(pady=10)

# Enhanced Games - All Working Perfectly
class SpaceShooterGame(EnhancedWindow):
    def __init__(self, master):
        super().__init__(master, "Space Shooter", 500, 600)
        
        self.score = 0
        self.lives = 3
        self.game_running = False
        self.player_x = 250
        self.bullets = []
        self.enemies = []
        
        self.setup_game()
    
    def setup_game(self):
        # Enhanced game header
        header = tk.Frame(self.content, bg='#2a2a4a', height=70)
        header.pack(fill='x', padx=10, pady=10)
        header.pack_propagate(False)
        
        self.score_label = tk.Label(header, text=f"SCORE: {self.score}",
                                   font=('Arial', 18, 'bold'),
                                   bg='#2a2a4a', fg='#00ffff')
        self.score_label.pack(side='left', padx=20)
        
        self.lives_label = tk.Label(header, text=f"LIVES: {self.lives}",
                                   font=('Arial', 18, 'bold'),
                                   bg='#2a2a4a', fg='#ff4444')
        self.lives_label.pack(side='right', padx=20)
        
        self.start_btn = tk.Button(header, text="START MISSION",
                                  command=self.toggle_game,
                                  font=('Arial', 12, 'bold'),
                                  bg='#ff00ff', fg='white')
        TouchOptimizer.make_touch_friendly(self.start_btn)
        self.start_btn.pack(side='top', pady=5)
        
        # Enhanced game canvas
        self.game_canvas = tk.Canvas(self.content, bg='#00001a',
                                    highlightthickness=0)
        self.game_canvas.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.setup_controls()
        self.draw_game()
    
    def setup_controls(self):
        self.game_canvas.bind('<Button-1>', self.shoot)
        self.game_canvas.bind('<B1-Motion>', self.move_player)
        self.game_canvas.focus_set()
    
    def move_player(self, event):
        if self.game_running:
            self.player_x = max(20, min(480, event.x))
            self.draw_game()
    
    def shoot(self, event):
        if self.game_running and len(self.bullets) < 3:
            self.bullets.append([self.player_x, 550])
            self.draw_game()
    
    def draw_game(self):
        self.game_canvas.delete('all')
        
        # Draw player (spaceship)
        self.game_canvas.create_polygon(
            self.player_x, 530,
            self.player_x - 25, 580,
            self.player_x + 25, 580,
            fill='#00ffff', outline='#0088ff', width=3
        )
        
        # Draw engine glow
        self.game_canvas.create_polygon(
            self.player_x - 10, 580,
            self.player_x, 600,
            self.player_x + 10, 580,
            fill='#ffff00', outline=''
        )
        
        # Draw bullets
        for bullet in self.bullets:
            x, y = bullet
            self.game_canvas.create_oval(x-4, y-4, x+4, y+4, fill='#ffff00')
            self.game_canvas.create_oval(x-2, y-2, x+2, y+2, fill='#ffffff')
        
        # Draw enemies
        for enemy in self.enemies:
            x, y = enemy
            self.game_canvas.create_rectangle(x-20, y-20, x+20, y+20, 
                                            fill='#ff4444', outline='#ff8888', width=2)
            self.game_canvas.create_polygon(x, y-25, x-15, y-5, x+15, y-5,
                                          fill='#ff0000', outline='')
    
    def toggle_game(self):
        self.game_running = not self.game_running
        if self.game_running:
            self.start_btn.config(text="PAUSE MISSION")
            self.score = 0
            self.lives = 3
            self.bullets = []
            self.enemies = []
            self.update_display()
            self.game_loop()
        else:
            self.start_btn.config(text="RESUME MISSION")
    
    def update_display(self):
        self.score_label.config(text=f"SCORE: {self.score}")
        self.lives_label.config(text=f"LIVES: {self.lives}")
    
    def game_loop(self):
        if not self.game_running:
            return
        
        # Spawn enemies
        if random.random() > 0.85:
            x = random.randint(40, 460)
            self.enemies.append([x, -40])
        
        # Move bullets
        for bullet in self.bullets[:]:
            bullet[1] -= 12
            if bullet[1] < 0:
                self.bullets.remove(bullet)
        
        # Move enemies and check collisions
        for enemy in self.enemies[:]:
            enemy[1] += 4
            
            # Check bullet collision
            for bullet in self.bullets[:]:
                if (abs(bullet[0] - enemy[0]) < 24 and 
                    abs(bullet[1] - enemy[1]) < 24):
                    if enemy in self.enemies and bullet in self.bullets:
                        self.enemies.remove(enemy)
                        self.bullets.remove(bullet)
                        self.score += 150
                        self.update_display()
                        break
            
            # Check player collision
            if (abs(self.player_x - enemy[0]) < 45 and 
                abs(550 - enemy[1]) < 45):
                if enemy in self.enemies:
                    self.enemies.remove(enemy)
                    self.lives -= 1
                    self.update_display()
                    if self.lives <= 0:
                        self.game_over()
                        return
            
            # Remove off-screen enemies
            if enemy[1] > 600 and enemy in self.enemies:
                self.enemies.remove(enemy)
        
        self.draw_game()
        if self.game_running:
            self.window.after(40, self.game_loop)
    
    def game_over(self):
        self.game_running = False
        self.start_btn.config(text="START MISSION")
        messagebox.showinfo("Mission Failed", f"Final Score: {self.score}\nBetter luck next time!")

class QuantumRunnerGame(EnhancedWindow):
    def __init__(self, master):
        super().__init__(master, "Quantum Runner", 500, 600)
        
        self.score = 0
        self.game_running = False
        self.player_y = 300
        self.obstacles = []
        self.jump_velocity = 0
        self.jumping = False
        
        self.setup_game()
    
    def setup_game(self):
        # Enhanced game header
        header = tk.Frame(self.content, bg='#2a2a4a', height=60)
        header.pack(fill='x', padx=10, pady=10)
        header.pack_propagate(False)
        
        self.score_label = tk.Label(header, text=f"DISTANCE: {self.score}",
                                   font=('Arial', 18, 'bold'),
                                   bg='#2a2a4a', fg='#00ffff')
        self.score_label.pack(side='left', padx=20)
        
        self.start_btn = tk.Button(header, text="START RUN",
                                  command=self.toggle_game,
                                  font=('Arial', 14, 'bold'),
                                  bg='#ff00ff', fg='white')
        TouchOptimizer.make_touch_friendly(self.start_btn)
        self.start_btn.pack(side='right', padx=20)
        
        # Enhanced game canvas
        self.game_canvas = tk.Canvas(self.content, bg='#0a0a2a',
                                    highlightthickness=0)
        self.game_canvas.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.setup_controls()
        self.draw_game()
    
    def setup_controls(self):
        self.game_canvas.bind('<Button-1>', self.jump)
        self.game_canvas.focus_set()
    
    def jump(self, event):
        if self.game_running and not self.jumping:
            self.jumping = True
            self.jump_velocity = -18
    
    def draw_game(self):
        self.game_canvas.delete('all')
        
        # Draw ground
        self.game_canvas.create_rectangle(0, 400, 500, 600, fill='#334455')
        for i in range(0, 500, 20):
            self.game_canvas.create_line(i, 400, i+10, 400, fill='#556677', width=2)
        
        # Draw player
        self.game_canvas.create_rectangle(100, self.player_y-25, 130, self.player_y,
                                         fill='#00ffff', outline='#0088ff', width=3)
        # Player details
        self.game_canvas.create_oval(105, self.player_y-20, 115, self.player_y-10, fill='#ffffff')
        self.game_canvas.create_oval(115, self.player_y-20, 125, self.player_y-10, fill='#ffffff')
        
        # Draw obstacles
        for obstacle in self.obstacles:
            x, height, obs_type = obstacle
            if obs_type == "high":
                color = '#ff4444'
            else:
                color = '#ff8800'
            
            self.game_canvas.create_rectangle(x, 400-height, x+35, 400,
                                            fill=color, outline='#ffaaaa', width=2)
    
    def toggle_game(self):
        self.game_running = not self.game_running
        if self.game_running:
            self.start_btn.config(text="PAUSE RUN")
            self.score = 0
            self.player_y = 300
            self.obstacles = []
            self.jumping = False
            self.update_display()
            self.game_loop()
        else:
            self.start_btn.config(text="RESUME RUN")
    
    def update_display(self):
        self.score_label.config(text=f"DISTANCE: {self.score}")
    
    def game_loop(self):
        if not self.game_running:
            return
        
        # Handle jumping physics
        if self.jumping:
            self.player_y += self.jump_velocity
            self.jump_velocity += 0.9
            if self.player_y >= 300:
                self.player_y = 300
                self.jumping = False
                self.jump_velocity = 0
        
        # Spawn obstacles
        if random.random() > 0.92:
            height = random.randint(40, 120)
            obs_type = "high" if height > 80 else "low"
            self.obstacles.append([500, height, obs_type])
        
        # Move obstacles
        for obstacle in self.obstacles[:]:
            obstacle[0] -= 6
            
            # Check collision
            if (obstacle[0] < 130 and obstacle[0] > 70 and 
                self.player_y > 400 - obstacle[1]):
                self.game_over()
                return
            
            # Remove off-screen obstacles and score
            if obstacle[0] < -35:
                self.obstacles.remove(obstacle)
                self.score += 5
                self.update_display()
        
        self.draw_game()
        if self.game_running:
            self.window.after(35, self.game_loop)
    
    def game_over(self):
        self.game_running = False
        self.start_btn.config(text="START RUN")
        messagebox.showinfo("Run Ended", f"Final Distance: {self.score} meters!\nGreat run!")

class PuzzleGame(EnhancedWindow):
    def __init__(self, master):
        super().__init__(master, "Puzzle Challenge", 400, 500)
        self.setup_game()
    
    def setup_game(self):
        self.moves = 0
        self.game_completed = False
        
        # Header
        header = tk.Frame(self.content, bg='#2a2a4a', height=60)
        header.pack(fill='x', padx=10, pady=10)
        header.pack_propagate(False)
        
        self.moves_label = tk.Label(header, text=f"MOVES: {self.moves}",
                                   font=('Arial', 16, 'bold'),
                                   bg='#2a2a4a', fg='#00ffff')
        self.moves_label.pack(side='left', padx=20)
        
        self.start_btn = tk.Button(header, text="NEW GAME",
                                  command=self.new_game,
                                  font=('Arial', 12, 'bold'),
                                  bg='#ff00ff', fg='white')
        TouchOptimizer.make_touch_friendly(self.start_btn)
        self.start_btn.pack(side='right', padx=20)
        
        # Puzzle grid
        self.puzzle_frame = tk.Frame(self.content, bg='#1a1a3a')
        self.puzzle_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        self.tiles = []
        self.empty_pos = (3, 3)
        self.create_puzzle_grid()
        self.new_game()
    
    def create_puzzle_grid(self):
        for i in range(4):
            for j in range(4):
                tile = tk.Label(self.puzzle_frame, text="", 
                               font=('Arial', 20, 'bold'),
                               bg='#00ffff', fg='#000033',
                               width=4, height=2,
                               relief='raised', bd=3)
                tile.grid(row=i, column=j, padx=2, pady=2)
                tile.bind('<Button-1>', lambda e, row=i, col=j: self.move_tile(row, col))
                self.tiles.append((tile, i, j))
    
    def new_game(self):
        self.moves = 0
        self.game_completed = False
        self.moves_label.config(text=f"MOVES: {self.moves}")
        
        # Initialize tiles
        numbers = list(range(1, 16)) + [""]
        random.shuffle(numbers)
        
        for idx, (tile, row, col) in enumerate(self.tiles):
            num = numbers[idx]
            if num:
                tile.config(text=str(num), bg='#00ffff', state='normal')
            else:
                tile.config(text="", bg='#2a2a4a', state='disabled')
                self.empty_pos = (row, col)
    
    def move_tile(self, row, col):
        if self.game_completed:
            return
            
        empty_row, empty_col = self.empty_pos
        
        # Check if move is valid (adjacent to empty space)
        if ((abs(row - empty_row) == 1 and col == empty_col) or 
            (abs(col - empty_col) == 1 and row == empty_row)):
            
            # Find the clicked tile
            for tile, t_row, t_col in self.tiles:
                if t_row == row and t_col == col:
                    # Swap with empty space
                    empty_tile = None
                    for et, er, ec in self.tiles:
                        if er == empty_row and ec == empty_col:
                            empty_tile = et
                            break
                    
                    if empty_tile:
                        # Swap text and colors
                        empty_tile.config(text=tile.cget('text'), bg='#00ffff', state='normal')
                        tile.config(text="", bg='#2a2a4a', state='disabled')
                        
                        self.empty_pos = (row, col)
                        self.moves += 1
                        self.moves_label.config(text=f"MOVES: {self.moves}")
                        
                        self.check_win()
                    break
    
    def check_win(self):
        current_order = []
        for tile, row, col in sorted(self.tiles, key=lambda x: (x[1], x[2])):
            current_order.append(tile.cget('text'))
        
        expected_order = [str(i) for i in range(1, 16)] + [""]
        
        if current_order == expected_order:
            self.game_completed = True
            messagebox.showinfo("Puzzle Solved!", f"Congratulations! You solved the puzzle in {self.moves} moves!")

class MemoryCardGame(EnhancedWindow):
    def __init__(self, master):
        super().__init__(master, "Memory Cards", 500, 500)
        self.setup_game()
    
    def setup_game(self):
        self.score = 0
        self.flipped_cards = []
        self.matched_pairs = 0
        self.can_flip = True
        
        # Header
        header = tk.Frame(self.content, bg='#2a2a4a', height=60)
        header.pack(fill='x', padx=10, pady=10)
        header.pack_propagate(False)
        
        self.score_label = tk.Label(header, text=f"SCORE: {self.score}",
                                   font=('Arial', 16, 'bold'),
                                   bg='#2a2a4a', fg='#00ffff')
        self.score_label.pack(side='left', padx=20)
        
        self.start_btn = tk.Button(header, text="NEW GAME",
                                  command=self.new_game,
                                  font=('Arial', 12, 'bold'),
                                  bg='#ff00ff', fg='white')
        TouchOptimizer.make_touch_friendly(self.start_btn)
        self.start_btn.pack(side='right', padx=20)
        
        # Game grid
        self.game_frame = tk.Frame(self.content, bg='#1a1a3a')
        self.game_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        self.cards = []
        self.card_values = []
        self.create_card_grid()
        self.new_game()
    
    def create_card_grid(self):
        for i in range(4):
            for j in range(4):
                card = tk.Button(self.game_frame, text="?", 
                               font=('Arial', 16, 'bold'),
                               bg='#ff00ff', fg='white',
                               width=6, height=3,
                               command=lambda row=i, col=j: self.flip_card(row, col))
                card.grid(row=i, column=j, padx=2, pady=2)
                self.cards.append((card, i, j))
    
    def new_game(self):
        self.score = 0
        self.matched_pairs = 0
        self.flipped_cards = []
        self.can_flip = True
        self.score_label.config(text=f"SCORE: {self.score}")
        
        # Create pairs of numbers
        numbers = list(range(1, 9)) * 2
        random.shuffle(numbers)
        self.card_values = numbers
        
        # Reset all cards
        for idx, (card, row, col) in enumerate(self.cards):
            card.config(text="?", bg='#ff00ff', state='normal')
    
    def flip_card(self, row, col):
        if not self.can_flip or len(self.flipped_cards) >= 2:
            return
        
        # Find the clicked card
        for idx, (card, c_row, c_col) in enumerate(self.cards):
            if c_row == row and c_col == col:
                if card in [fc[0] for fc in self.flipped_cards]:
                    return  # Card already flipped
                
                # Show card value
                value = self.card_values[idx]
                card.config(text=str(value), bg='#00ffff')
                self.flipped_cards.append((card, value, idx))
                
                if len(self.flipped_cards) == 2:
                    self.check_match()
                break
    
    def check_match(self):
        if len(self.flipped_cards) == 2:
            self.can_flip = False
            card1, value1, idx1 = self.flipped_cards[0]
            card2, value2, idx2 = self.flipped_cards[1]
            
            if value1 == value2:
                # Match found
                self.score += 10
                self.matched_pairs += 1
                self.score_label.config(text=f"SCORE: {self.score}")
                
                card1.config(bg='#00ff00', state='disabled')
                card2.config(bg='#00ff00', state='disabled')
                self.flipped_cards = []
                self.can_flip = True
                
                if self.matched_pairs == 8:
                    messagebox.showinfo("Game Over!", f"Congratulations! You won with {self.score} points!")
            else:
                # No match
                self.window.after(1000, self.hide_cards)
    
    def hide_cards(self):
        for card, value, idx in self.flipped_cards:
            card.config(text="?", bg='#ff00ff')
        self.flipped_cards = []
        self.can_flip = True

# Enhanced Effects
class EnhancedShotgunEffect:
    def __init__(self, master):
        self.master = master
        self.create_enhanced_effect()
    
    def create_enhanced_effect(self):
        self.effect_window = tk.Toplevel(self.master)
        self.effect_window.attributes('-fullscreen', True, '-alpha', 0.0)
        self.effect_window.configure(bg='#000000')
        self.effect_window.overrideredirect(True)
        
        self.effect_canvas = tk.Canvas(self.effect_window, bg='#000000',
                                      highlightthickness=0)
        self.effect_canvas.pack(fill='both', expand=True)
        
        self.execute_enhanced_effect()
    
    def execute_enhanced_effect(self):
        def phase1():
            self.effect_canvas.create_text(MOBILE_WIDTH//2, MOBILE_HEIGHT//2,
                                          text="QUANTUM SHOTGUN!",
                                          font=('Arial', 52, 'bold'),
                                          fill='#ff4444')
            self.effect_window.attributes('-alpha', 1.0)
            self.effect_window.after(200, phase2)
        
        def phase2():
            self.effect_canvas.delete('all')
            # Add particle effects
            for _ in range(20):
                x = random.randint(100, MOBILE_WIDTH-100)
                y = random.randint(100, MOBILE_HEIGHT-100)
                size = random.randint(10, 30)
                self.effect_canvas.create_oval(x, y, x+size, y+size, 
                                             fill='#ff8800', outline='')
            
            self.effect_canvas.create_text(MOBILE_WIDTH//2, MOBILE_HEIGHT//2,
                                          text="BOOM!",
                                          font=('Arial', 42, 'bold'),
                                          fill='#ffff00')
            self.effect_window.after(200, phase3)
        
        def phase3():
            self.effect_canvas.delete('all')
            self.effect_canvas.create_text(MOBILE_WIDTH//2, MOBILE_HEIGHT//2,
                                          text="EFFECT COMPLETE",
                                          font=('Arial', 32),
                                          fill='#00ffff')
            self.effect_window.after(300, self.close_enhanced_effect)
        
        phase1()
    
    def close_enhanced_effect(self):
        alpha = 1.0
        def fade_out():
            nonlocal alpha
            if alpha > 0:
                alpha -= 0.1
                self.effect_window.attributes('-alpha', alpha)
                self.effect_window.after(25, fade_out)
            else:
                self.effect_window.destroy()
        fade_out()

class EnhancedShutdownSequence:
    def __init__(self, master):
        self.master = master
        self.execute_enhanced_shutdown()
    
    def execute_enhanced_shutdown(self):
        self.shutdown_window = tk.Toplevel(self.master)
        self.shutdown_window.attributes('-fullscreen', True, '-alpha', 0.0)
        self.shutdown_window.configure(bg='#000010')
        self.shutdown_window.overrideredirect(True)
        
        self.shutdown_canvas = tk.Canvas(self.shutdown_window, bg='#000010',
                                        highlightthickness=0)
        self.shutdown_canvas.pack(fill='both', expand=True)
        
        self.enhanced_shutdown_sequence()
    
    def enhanced_shutdown_sequence(self):
        def step1():
            self.shutdown_canvas.create_text(MOBILE_WIDTH//2, MOBILE_HEIGHT//2,
                                           text="Initiating System Shutdown",
                                           font=('Arial', 22),
                                           fill='#00ffff')
            self.shutdown_window.attributes('-alpha', 1.0)
            self.shutdown_window.after(800, step2)
        
        def step2():
            self.shutdown_canvas.delete('all')
            self.shutdown_canvas.create_text(MOBILE_WIDTH//2, MOBILE_HEIGHT//2,
                                           text="Saving all data...",
                                           font=('Arial', 20),
                                           fill='#ffff00')
            self.shutdown_window.after(800, step3)
        
        def step3():
            self.shutdown_canvas.delete('all')
            self.shutdown_canvas.create_text(MOBILE_WIDTH//2, MOBILE_HEIGHT//2,
                                           text="Closing applications...",
                                           font=('Arial', 20),
                                           fill='#ff8800')
            self.shutdown_window.after(800, step4)
        
        def step4():
            self.shutdown_canvas.delete('all')
            self.shutdown_canvas.create_text(MOBILE_WIDTH//2, MOBILE_HEIGHT//2,
                                           text="Goodbye",
                                           font=('Arial', 28, 'bold'),
                                           fill='#00ffff')
            self.shutdown_window.after(1200, step5)
        
        def step5():
            self.master.quit()
        
        step1()

# Start the enhanced system
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Quantum OS - Premium Edition")
    root.geometry(f"{MOBILE_WIDTH}x{MOBILE_HEIGHT}")
    root.resizable(False, False)
    
    ModernBootScreen(root)
    root.mainloop()