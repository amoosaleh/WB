import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog, simpledialog
import sqlite3
import threading
import time
from datetime import datetime
import random
import math
import json
from PIL import Image, ImageDraw, ImageTk
import os
import shutil

# سیستم مدیریت تم
class ThemeManager:
    def __init__(self):
        self.themes = {
            'quantum': {
                'bg': '#0a0a0a',
                'fg': '#00ffff',
                'accent': '#ff44ff',
                'secondary': '#00ff88',
                'text': '#ffffff',
                'header_bg': '#1a1a1a',
                'widget_bg': '#151515',
                'button_bg': '#252525',
                'success': '#00ff88',
                'warning': '#ffff00',
                'error': '#ff4444'
            },
            'dark': {
                'bg': '#1a1a1a',
                'fg': '#ffffff', 
                'accent': '#ff8800',
                'secondary': '#0088ff',
                'text': '#ffffff',
                'header_bg': '#2a2a2a',
                'widget_bg': '#252525',
                'button_bg': '#353535',
                'success': '#00aa00',
                'warning': '#ffaa00',
                'error': '#ff4444'
            },
            'blue': {
                'bg': '#001122',
                'fg': '#00ffff',
                'accent': '#ff4444',
                'secondary': '#00ff88',
                'text': '#ffffff',
                'header_bg': '#002244',
                'widget_bg': '#001933',
                'button_bg': '#003366',
                'success': '#00ff88',
                'warning': '#ffff00',
                'error': '#ff4444'
            },
            'purple': {
                'bg': '#110011',
                'fg': '#ff44ff',
                'accent': '#00ffff',
                'secondary': '#ffff00',
                'text': '#ffffff',
                'header_bg': '#220022',
                'widget_bg': '#1a001a',
                'button_bg': '#330033',
                'success': '#00ff88',
                'warning': '#ffff00',
                'error': '#ff4444'
            },
            'green': {
                'bg': '#001100',
                'fg': '#00ff88',
                'accent': '#ff44ff',
                'secondary': '#00ffff',
                'text': '#ffffff',
                'header_bg': '#002200',
                'widget_bg': '#001a00',
                'button_bg': '#003300',
                'success': '#00ff88',
                'warning': '#ffff00',
                'error': '#ff4444'
            }
        }
        self.current_theme = 'quantum'
        self.theme_list = list(self.themes.keys())
        
    def get_theme(self):
        return self.themes[self.current_theme]
    
    def change_theme(self):
        current_index = self.theme_list.index(self.current_theme)
        next_index = (current_index + 1) % len(self.theme_list)
        self.current_theme = self.theme_list[next_index]
        return self.get_theme()

# کلاس پایه برای تمام برنامه‌ها
class QuantumApp:
    def __init__(self, os):
        self.os = os
        self.window = None
        
    def apply_theme(self, widget=None):
        theme = self.os.theme_manager.get_theme()
        if widget is None:
            widget = self.window
            
        try:
            if isinstance(widget, tk.Tk) or isinstance(widget, tk.Toplevel):
                widget.configure(bg=theme['bg'])
            
            for child in widget.winfo_children():
                self.apply_theme_to_child(child, theme)
        except:
            pass
            
    def apply_theme_to_child(self, widget, theme):
        try:
            widget_type = widget.winfo_class()
            
            if widget_type in ['Frame', 'Labelframe', 'LabelFrame']:
                widget.configure(bg=theme['bg'])
            elif widget_type == 'Label':
                if 'title' in str(widget).lower() or 'header' in str(widget).lower():
                    widget.configure(bg=theme['header_bg'], fg=theme['fg'])
                else:
                    widget.configure(bg=theme['bg'], fg=theme['text'])
            elif widget_type == 'Button':
                widget.configure(bg=theme['button_bg'], fg=theme['text'])
            elif widget_type == 'Entry':
                widget.configure(bg=theme['widget_bg'], fg=theme['text'])
            elif widget_type == 'Text':
                widget.configure(bg=theme['widget_bg'], fg=theme['text'])
            elif widget_type == 'Canvas':
                widget.configure(bg=theme['bg'])
            elif widget_type == 'Scrollbar':
                widget.configure(bg=theme['button_bg'])
                
            for child in widget.winfo_children():
                self.apply_theme_to_child(child, theme)
        except:
            pass

# Neural Cache System
class NeuralCache:
    def __init__(self):
        self.patterns = {}
        self.activation_levels = {}
        
    def store_pattern(self, pattern, activation):
        self.patterns[pattern] = activation
        
    def get_activation(self, pattern):
        return self.patterns.get(pattern, 0.0)

# Quantum AI Processor
class QuantumAIProcessor:
    def __init__(self):
        self.quantum_memory = []
        self.neural_weights = {}
        
    def process_quantum_query(self, query):
        responses = {
            'quantum': [
                "Quantum state analysis complete",
                "Neural network processing engaged",
                "Quantum coherence established",
                "Temporal synchronization optimal"
            ],
            'system': [
                "Quantum systems operating at 99.8% efficiency",
                "Neural throughput: 450 GQ/s",
                "Temporal stability: 99.9%",
                "Quantum encryption: active"
            ],
            'compute': self.quantum_computation,
            'time': lambda: f"Quantum temporal analysis: {datetime.now().strftime('%H:%M:%S')}",
            'help': "Available commands: quantum, system, time, compute, help"
        }
        
        query = query.lower()
        for key in responses:
            if key in query:
                if callable(responses[key]):
                    return responses[key]()
                return random.choice(responses[key])
        
        return "Quantum processing complete. Neural networks engaged."

    def quantum_computation(self):
        numbers = [random.uniform(1, 100) for _ in range(3)]
        result = sum(numbers) * random.uniform(0.99, 1.01)
        return f"Quantum computation result: {result:.6f}"

# Quantum Widgets
class QuantumWidget:
    def __init__(self, parent, title):
        self.parent = parent
        self.title = title
        self.frame = None
        self.quantum_state = 0.0
        
    def create(self):
        self.frame = tk.Frame(self.parent, bg='#151515', relief='flat', bd=1)
        self.create_quantum_header()
        self.create_quantum_content()
        return self.frame
        
    def create_quantum_header(self):
        header = tk.Frame(self.frame, bg='#252525')
        header.pack(fill='x')
        tk.Label(header, text=self.title, font=('Arial', 9, 'bold'),
                bg='#252525', fg='#00ffff').pack(padx=8, pady=4)
        
    def create_quantum_content(self):
        self.content = tk.Frame(self.frame, bg='#151515')
        self.content.pack(fill='both', expand=True, padx=10, pady=8)
        
    def quantum_update(self):
        self.quantum_state = (self.quantum_state + 0.1) % 1.0

class NeuralWeatherWidget(QuantumWidget):
    def __init__(self, parent):
        super().__init__(parent, "NEURAL WEATHER")
        
    def create_quantum_content(self):
        super().create_quantum_content()
        
        self.temp_label = tk.Label(self.content, text="24.7°C", 
                                 font=('Arial', 14, 'bold'),
                                 bg='#151515', fg='white')
        self.temp_label.pack()
        
        self.condition_label = tk.Label(self.content, text="QUANTUM STABLE", 
                                      font=('Arial', 8),
                                      bg='#151515', fg='#cccccc')
        self.condition_label.pack()
        
        self.pressure_label = tk.Label(self.content, text="1015 hPa", 
                                     font=('Arial', 7),
                                     bg='#151515', fg='#888888')
        self.pressure_label.pack()
        
    def quantum_update(self):
        super().quantum_update()
        new_temp = 20 + 10 * math.sin(self.quantum_state * math.pi * 2)
        conditions = ["QUANTUM STABLE", "NEURAL CALM", "AI OPTIMIZED", "COHERENT"]
        
        self.temp_label.config(text=f"{new_temp:.1f}°C")
        self.condition_label.config(text=random.choice(conditions))
        self.pressure_label.config(text=f"{1000 + random.randint(0, 30)} hPa")

class QuantumHealthWidget(QuantumWidget):
    """Quantum health monitoring"""
    def __init__(self, parent):
        super().__init__(parent, "QUANTUM HEALTH")
        
    def create_quantum_content(self):
        super().create_quantum_content()
        
        self.metrics = {
            'vitals': tk.Label(self.content, text="VITALS: 98.5%", font=('Arial', 8), bg='#151515', fg='#00ff88'),
            'neural': tk.Label(self.content, text="NEURAL: 95.2%", font=('Arial', 7), bg='#151515', fg='#ff44ff'),
            'quantum': tk.Label(self.content, text="QUANTUM: 99.1%", font=('Arial', 7), bg='#151515', fg='#ffff00')
        }
        
        for label in self.metrics.values():
            label.pack(anchor='w')
            
    def quantum_update(self):
        super().quantum_update()
        # Update health metrics
        self.metrics['vitals'].config(text=f"VITALS: {98 + random.randint(-1, 1)}.{random.randint(0,9)}%")
        self.metrics['neural'].config(text=f"NEURAL: {95 + random.randint(-1, 1)}.{random.randint(0,9)}%")
        self.metrics['quantum'].config(text=f"QUANTUM: {99 + random.randint(-1, 0)}.{random.randint(0,9)}%")

class AIFinanceWidget(QuantumWidget):
    """AI-powered financial analysis"""
    def __init__(self, parent):
        super().__init__(parent, "QUANTUM FINANCE")
        
    def create_quantum_content(self):
        super().create_quantum_content()
        
        self.index_label = tk.Label(self.content, text="QFI: 1548.2", 
                                  font=('Arial', 10, 'bold'),
                                  bg='#151515', fg='#00ff88')
        self.index_label.pack()
        
        self.trend_label = tk.Label(self.content, text="NEURAL BULLISH", 
                                  font=('Arial', 7),
                                  bg='#151515', fg='#cccccc')
        self.trend_label.pack()
        
        self.prediction_label = tk.Label(self.content, text="+2.8% QUANTUM", 
                                       font=('Arial', 7),
                                       bg='#151515', fg='#ffff00')
        self.prediction_label.pack()
        
    def quantum_update(self):
        super().quantum_update()
        # Update financial data
        base_index = 1500 + random.uniform(-50, 100)
        change = random.uniform(-3.0, 5.0)
        trends = ["NEURAL BULLISH", "QUANTUM STABLE", "AI OPTIMIZED"]
        
        self.index_label.config(text=f"QFI: {base_index:.1f}")
        self.trend_label.config(text=random.choice(trends))
        self.prediction_label.config(text=f"{change:+.1f}% QUANTUM")

class SystemMonitorWidget(QuantumWidget):
    """Quantum system monitor"""
    def __init__(self, parent):
        super().__init__(parent, "SYSTEM QUANTUM")
        
    def create_quantum_content(self):
        super().create_quantum_content()
        
        self.metrics = {
            'cpu': tk.Label(self.content, text="CPU: 18.5%", font=('Arial', 7), bg='#151515', fg='#ff4444'),
            'memory': tk.Label(self.content, text="RAM: 42.3%", font=('Arial', 7), bg='#151515', fg='#ff9900'),
            'quantum': tk.Label(self.content, text="Q-BITS: 512", font=('Arial', 7), bg='#151515', fg='#00ffff')
        }
        
        for label in self.metrics.values():
            label.pack(anchor='w')
            
    def quantum_update(self):
        super().quantum_update()
        # Update system metrics
        self.metrics['cpu'].config(text=f"CPU: {random.randint(5, 25)}.{random.randint(0,9)}%")
        self.metrics['memory'].config(text=f"RAM: {random.randint(40, 65)}.{random.randint(0,9)}%")
        self.metrics['quantum'].config(text=f"Q-BITS: {500 + random.randint(0, 50)}")

# کلاس اصلی سیستم عامل
class QuantumMobileOS:
    def __init__(self):
        self.screen_width = 360
        self.screen_height = 740
        
        self.root = tk.Tk()
        self.root.title("Quantum OS v4.0 ⚛- Created by Saleh Amoo")
        self.root.geometry(f"{self.screen_width}x{self.screen_height}")
        self.root.configure(bg='#0a0a0a')
        self.root.resizable(False, False)
        
        self.root.withdraw()
        
        self.theme_manager = ThemeManager()
        
        self.animation_running = False
        self.current_directory = os.path.expanduser("~")
        
        # اضافه کردن ویژگی‌های گم شده
        self.quantum_state = "superposition"
        self.neural_activity = 0.85
        self.quantum_entanglement = 0.92
        
        self.setup_quantum_core()
        self.setup_neural_interface()
        self.start_quantum_services()

    def setup_quantum_core(self):
        self.quantum_settings = {
            'quantum_processing': True,
            'neural_networks': True,
            'holographic_display': False,
            'temporal_sync': True,
            'quantum_encryption': True
        }
        
        self.setup_quantum_database()
        self.neural_cache = NeuralCache()
        self.quantum_ai = QuantumAIProcessor()
        
        self.system_metrics = {
            'quantum_coherence': 98.7,
            'neural_throughput': 450,
            'temporal_stability': 99.9,
            'quantum_efficiency': 87.3
        }

    def setup_quantum_database(self):
        self.quantum_db = sqlite3.connect(':memory:', check_same_thread=False)
        self.q_cursor = self.quantum_db.cursor()
        
        self.q_cursor.execute('''
            CREATE TABLE IF NOT EXISTS quantum_apps (
                id INTEGER PRIMARY KEY,
                name TEXT,
                quantum_signature TEXT,
                neural_compatibility REAL,
                processing_tier INTEGER,
                version TEXT
            )
        ''')
        
        self.initialize_quantum_data()

    def initialize_quantum_data(self):
        quantum_apps = [
            ('Quantum Phone', 'QCOM001', 0.95, 3, '4.2'),
            #('Neural Messenger', 'NMSG002', 0.92, 2, '3.8'),
            ('AI Camera', 'AVIS003', 0.98, 4, '5.1'),
          #  ('Quantum Browser', 'QBRO004', 0.89, 2, '3.5'),
            ('Quantum Calculator', 'QCAL005', 0.94, 3, '4.0'),
            ('Temporal Calendar', 'TCAL006', 0.97, 4, '4.8'),
            ('Quantum AI', 'QAI007', 0.96, 3, '4.1'),
           # ('Neural Files', 'NFIL008', 0.91, 2, '3.3'),
          #  ('Quantum Music', 'QMUS009', 0.93, 3, '4.2'),
            ('Neural Health', 'NHLT010', 0.90, 2, '3.0'),
            ('Quantum Finance', 'QFIN011', 0.88, 2, '2.8'),
            ('System Control', 'SCTL012', 0.99, 5, '6.0'),
            ('Shutdown', 'SHTD013', 0.99, 1, '1.0'),
            ('Number Game', 'GAME014', 0.85, 1, '2.0'),
            ('Tic Tac Toe', 'GAME015', 0.88, 1, '2.1'),
            ('BY SALEH AMOO', 'Saleh Amoo', 0.89, 1, '2.2')
        ]
        
        for app in quantum_apps:
            self.q_cursor.execute('''
                INSERT INTO quantum_apps (name, quantum_signature, neural_compatibility, processing_tier, version)
                VALUES (?, ?, ?, ?, ?)
            ''', app)
        
        self.quantum_db.commit()

    def setup_neural_interface(self):
        self.setup_quantum_status()
        self.setup_quantum_interface()
        self.setup_neural_navigation()

    def setup_quantum_status(self):
        self.status_frame = tk.Frame(self.root, bg='#0f0f0f', height=35)
        self.status_frame.pack(fill='x')
        self.status_frame.pack_propagate(False)
        
        self.quantum_time = tk.Label(self.status_frame, text="", 
                                   font=('Arial', 9, 'bold'),
                                   bg='#0f0f0f', fg='#00ffff')
        self.quantum_time.pack(side='left', padx=12)
        
        self.coherence_label = tk.Label(self.status_frame, text="QC: 98.7%", font=('Arial', 8),
                        bg='#0f0f0f', fg='#00ff88')
        self.coherence_label.pack(side='right', padx=4)
        
        self.throughput_label = tk.Label(self.status_frame, text="NT: 450", font=('Arial', 8),
                        bg='#0f0f0f', fg='#ff44ff')
        self.throughput_label.pack(side='right', padx=4)
        
        self.stability_label = tk.Label(self.status_frame, text="TS: 99.9%", font=('Arial', 8),
                        bg='#0f0f0f', fg='#ffff00')
        self.stability_label.pack(side='right', padx=4)
        
        self.theme_btn = tk.Button(self.status_frame, text="THEME", font=('Arial', 7),
                                 bg='#252525', fg='#ff44ff', command=self.change_theme)
        self.theme_btn.pack(side='right', padx=4)
        
        self.shutdown_btn = tk.Button(self.status_frame, text="OFF", font=('Arial', 7),
                                    bg='#252525', fg='#ff4444', command=self.show_shutdown)
        self.shutdown_btn.pack(side='right', padx=4)
        
        # دکمه Created by Saleh Amoo
        self.credit_btn = tk.Button(self.status_frame, text="By Saleh Amoo", font=('Arial', 7),
                                  bg='#252525', fg='#00ff88', command=self.show_credits)
        self.credit_btn.pack(side='right', padx=4)
        
        self.update_quantum_status()

    def setup_quantum_interface(self):
        self.main_frame = tk.Frame(self.root, bg='#0a0a0a')
        self.main_frame.pack(fill='both', expand=True)
        
        self.setup_quantum_visualization()
        self.setup_neural_widgets()
        self.setup_quantum_apps()

    def setup_quantum_visualization(self):
        self.quantum_canvas = tk.Canvas(self.main_frame, bg='#0a0a0a', 
                                       height=180, highlightthickness=0)
        self.quantum_canvas.pack(fill='x', pady=(10, 5))
        
        self.quantum_particles = []
        self.wave_functions = []
        
        self.initialize_quantum_field()
        self.animate_quantum_field()

    def initialize_quantum_field(self):
        for _ in range(15):
            particle = {
                'x': random.uniform(50, 310),
                'y': random.uniform(30, 150),
                'vx': random.uniform(-1.5, 1.5),
                'vy': random.uniform(-1.5, 1.5),
                'spin': random.choice([-1, 1]),
                'energy': random.uniform(0.5, 2.0),
                'color': self.get_quantum_color()
            }
            self.quantum_particles.append(particle)
        
        for _ in range(3):
            wave = {
                'amplitude': random.uniform(15, 35),
                'frequency': random.uniform(0.03, 0.07),
                'phase': random.uniform(0, math.pi * 2),
                'wavelength': random.uniform(80, 150),
                'color': self.get_quantum_color()
            }
            self.wave_functions.append(wave)

    def get_quantum_color(self):
        colors = ['#00ffff', '#ff00ff', '#ffff00', '#00ff88', '#ff4444', '#8888ff']
        return random.choice(colors)

    def animate_quantum_field(self):
        if hasattr(self, 'quantum_canvas'):
            self.quantum_canvas.delete("quantum")
            
            for wave in self.wave_functions:
                points = []
                for x in range(0, 361, 5):
                    y = 90 + wave['amplitude'] * math.sin(wave['frequency'] * x + wave['phase'])
                    points.extend([x, y])
                
                self.quantum_canvas.create_line(points, fill=wave['color'], 
                                              width=1.5, tags="quantum", smooth=True)
                wave['phase'] += 0.1
            
            for particle in self.quantum_particles:
                particle['x'] += particle['vx'] + random.uniform(-0.3, 0.3)
                particle['y'] += particle['vy'] + random.uniform(-0.3, 0.3)
                
                if random.random() < 0.02:
                    particle['x'] = random.uniform(50, 310)
                    particle['y'] = random.uniform(30, 150)
                
                if particle['x'] < 20 or particle['x'] > 340:
                    particle['vx'] *= -1
                    particle['color'] = self.get_quantum_color()
                if particle['y'] < 20 or particle['y'] > 160:
                    particle['vy'] *= -1
                    particle['color'] = self.get_quantum_color()
                
                size = 2 + particle['energy']
                self.quantum_canvas.create_oval(
                    particle['x'] - size, particle['y'] - size,
                    particle['x'] + size, particle['y'] + size,
                    fill=particle['color'], outline='', tags="quantum"
                )
                
                if particle['spin'] > 0:
                    self.quantum_canvas.create_line(
                        particle['x'], particle['y'] - size - 2,
                        particle['x'], particle['y'] + size + 2,
                        fill=particle['color'], width=1, tags="quantum"
                    )
            
            self.quantum_canvas.create_text(180, 25, text="QUANTUM OS v4.0", 
                                          font=('Arial', 14, 'bold'),
                                          fill='white', tags="quantum")
            self.quantum_canvas.create_text(180, 45, text="Created by Saleh Amoo", 
                                          font=('Arial', 9),
                                          fill='#00ffff', tags="quantum")
            
            self.root.after(50, self.animate_quantum_field)

    def setup_neural_widgets(self):
        widgets_frame = tk.Frame(self.main_frame, bg='#0a0a0a', height=120)
        widgets_frame.pack(fill='x', pady=5)
        widgets_frame.pack_propagate(False)
        
        # اضافه کردن تمام ویجت‌های قبلی
        self.neural_widgets = [
            NeuralWeatherWidget(widgets_frame),
            QuantumHealthWidget(widgets_frame),
            AIFinanceWidget(widgets_frame),
            SystemMonitorWidget(widgets_frame)
        ]
        
        for i, widget in enumerate(self.neural_widgets):
            widget_frame = widget.create()
            if widget_frame:
                widget_frame.grid(row=0, column=i, padx=3, sticky='nsew')
                widgets_frame.grid_columnconfigure(i, weight=1)

    def setup_quantum_apps(self):
        apps_frame = tk.Frame(self.main_frame, bg='#0a0a0a')
        apps_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        quantum_apps = self.get_quantum_apps()
        
        for i, (name, signature, compatibility) in enumerate(quantum_apps):
            row = i // 4
            col = i % 4
            
            app_btn = tk.Button(apps_frame, text=f"{name}\nQ:{compatibility}", 
                              font=('Arial', 8),
                              bg='#151515', fg='#00ffff',
                              relief='flat', width=8, height=3,
                              command=lambda s=signature: self.launch_with_animation(s))
            app_btn.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')
            
            apps_frame.grid_columnconfigure(col, weight=1)
            apps_frame.grid_rowconfigure(row, weight=1)

    def get_quantum_apps(self):
        self.q_cursor.execute('SELECT name, quantum_signature, neural_compatibility FROM quantum_apps')
        return self.q_cursor.fetchall()

    def setup_neural_navigation(self):
        nav_frame = tk.Frame(self.root, bg='#151515', height=65)
        nav_frame.pack(fill='x', side='bottom')
        nav_frame.pack_propagate(False)
        
        nav_actions = [
            ("QUANTUM AI", lambda: self.launch_with_animation('QAI007')),
            ("PHONE", lambda: self.launch_with_animation('QCOM001')),
            ("MESSAGES", lambda: self.launch_with_animation('NMSG002')),
            ("BROWSER", lambda: self.launch_with_animation('QBRO004')),
            ("FILES", lambda: self.launch_with_animation('NFIL008'))
        ]
        
        for text, command in nav_actions:
            btn = tk.Button(nav_frame, text=text, font=('Arial', 8, 'bold'),
                          bg='#252525', fg='#00ff88',
                          relief='flat', command=command)
            btn.pack(side='left', expand=True, fill='both', padx=2)

    def show_credits(self):
        """نمایش اعتبارات"""
        messagebox.showinfo("Credits", 
                          "Quantum OS v4.0\n\n"
                          "Created by: Saleh Amoo\n\n"
                          "Quantum Computing Interface\n"
                          "Neural Network Integration\n"
                          "Advanced AI Systems\n"
                          "© 2025 All rights reserved")

    def change_theme(self):
        """تغییر تم کل سیستم"""
        new_theme = self.theme_manager.change_theme()
        theme = self.theme_manager.get_theme()
        
        # اعمال تم به پنجره اصلی
        self.apply_theme_to_all_widgets(self.root, theme)
        
        # اعمال تم به تمام پنجره‌های باز
        for window in self.root.winfo_children():
            if isinstance(window, tk.Toplevel):
                self.apply_theme_to_all_widgets(window, theme)
        
        messagebox.showinfo("Theme Changed", f"Theme changed to {self.theme_manager.current_theme.upper()}")

    def apply_theme_to_all_widgets(self, parent, theme):
        """اعمال تم به تمام ویجت‌ها"""
        try:
            # اعمال به والد
            if isinstance(parent, (tk.Tk, tk.Toplevel)):
                parent.configure(bg=theme['bg'])
            
            # اعمال به تمام فرزندان
            for child in parent.winfo_children():
                self.apply_theme_recursive(child, theme)
        except:
            pass

    def apply_theme_recursive(self, widget, theme):
        """اعمال تم به صورت بازگشتی"""
        try:
            widget_type = widget.winfo_class()
            
            if widget_type in ['Frame', 'Labelframe', 'LabelFrame']:
                widget.configure(bg=theme['bg'])
            elif widget_type == 'Label':
                current_text = widget.cget('text')
                if any(keyword in current_text.upper() for keyword in ['QUANTUM', 'NEURAL', 'AI', 'SYSTEM']):
                    widget.configure(bg=theme['header_bg'], fg=theme['fg'])
                else:
                    widget.configure(bg=theme['bg'], fg=theme['text'])
            elif widget_type == 'Button':
                current_text = widget.cget('text')
                if 'OFF' in current_text:
                    widget.configure(bg=theme['button_bg'], fg=theme['error'])
                elif 'THEME' in current_text:
                    widget.configure(bg=theme['button_bg'], fg=theme['accent'])
                else:
                    widget.configure(bg=theme['button_bg'], fg=theme['text'])
            elif widget_type == 'Entry':
                widget.configure(bg=theme['widget_bg'], fg=theme['text'], insertbackground=theme['text'])
            elif widget_type == 'Text':
                widget.configure(bg=theme['widget_bg'], fg=theme['text'])
            elif widget_type == 'Canvas':
                widget.configure(bg=theme['bg'])
            elif widget_type == 'Scrollbar':
                widget.configure(bg=theme['button_bg'])
            elif widget_type == 'Scale':
                widget.configure(bg=theme['bg'], fg=theme['text'])
                
            # اعمال به فرزندان
            for child in widget.winfo_children():
                self.apply_theme_recursive(child, theme)
        except:
            pass

    def show_boot_screen(self):
        self.boot_window = tk.Toplevel(self.root)
        self.boot_window.title("Quantum OS Booting...")
        self.boot_window.geometry(f"{self.screen_width}x{self.screen_height}")
        self.boot_window.configure(bg='#000000')
        self.boot_window.overrideredirect(True)
        
        self.boot_window.geometry(f"+{self.boot_window.winfo_screenwidth()//2 - self.screen_width//2}+{self.boot_window.winfo_screenheight()//2 - self.screen_height//2}")
        
        self.boot_canvas = tk.Canvas(self.boot_window, bg='#000000', 
                                   width=self.screen_width, height=self.screen_height,
                                   highlightthickness=0)
        self.boot_canvas.pack(fill='both', expand=True)
        
        self.boot_particles = []
        self.boot_waves = []
        self.boot_progress = 0
        self.boot_stage = 0
        
        self.initialize_boot_animation()
        self.animate_boot_sequence()

    def initialize_boot_animation(self):
        for _ in range(30):
            particle = {
                'x': random.uniform(0, self.screen_width),
                'y': random.uniform(0, self.screen_height),
                'vx': random.uniform(-2, 2),
                'vy': random.uniform(-2, 2),
                'size': random.uniform(1, 4),
                'color': random.choice(['#00ffff', '#ff00ff', '#ffff00', '#00ff88']),
                'pulse': random.uniform(0, math.pi * 2)
            }
            self.boot_particles.append(particle)
        
        for i in range(4):
            wave = {
                'amplitude': 20 + i * 10,
                'frequency': 0.02 + i * 0.01,
                'phase': i * math.pi / 2,
                'speed': 0.05 + i * 0.02,
                'color': ['#00ffff', '#ff00ff', '#ffff00', '#00ff88'][i]
            }
            self.boot_waves.append(wave)

    def animate_boot_sequence(self):
        self.boot_canvas.delete("boot")
        
        center_x, center_y = self.screen_width // 2, self.screen_height // 2
        
        for wave in self.boot_waves:
            points = []
            for x in range(0, self.screen_width + 10, 5):
                y = center_y + wave['amplitude'] * math.sin(wave['frequency'] * x + wave['phase'])
                points.extend([x, y])
            
            self.boot_canvas.create_line(points, fill=wave['color'], 
                                       width=2, tags="boot", smooth=True)
            wave['phase'] += wave['speed']
        
        for particle in self.boot_particles:
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['pulse'] += 0.1
            
            if particle['x'] < 0: particle['x'] = self.screen_width
            if particle['x'] > self.screen_width: particle['x'] = 0
            if particle['y'] < 0: particle['y'] = self.screen_height
            if particle['y'] > self.screen_height: particle['y'] = 0
            
            pulse_size = particle['size'] + math.sin(particle['pulse']) * 1.5
            
            self.boot_canvas.create_oval(
                particle['x'] - pulse_size, particle['y'] - pulse_size,
                particle['x'] + pulse_size, particle['y'] + pulse_size,
                fill=particle['color'], outline='', tags="boot"
            )
        
        self.draw_quantum_logo(center_x, center_y)
        self.draw_boot_progress()
        self.update_boot_sequence()
        
        if self.boot_stage < 100:
            self.boot_window.after(30, self.animate_boot_sequence)
        else:
            self.finish_boot_sequence()

    def draw_quantum_logo(self, center_x, center_y):
        radius = 60
        self.boot_canvas.create_oval(
            center_x - radius, center_y - radius,
            center_x + radius, center_y + radius,
            outline='#00ffff', width=3, tags="boot"
        )
        
        time_factor = time.time() * 2
        for i in range(3):
            angle = time_factor + i * 2 * math.pi / 3
            orbit_radius = radius + 15 + i * 10
            electron_x = center_x + orbit_radius * math.cos(angle)
            electron_y = center_y + orbit_radius * math.sin(angle)
            
            self.boot_canvas.create_oval(
                center_x - orbit_radius, center_y - orbit_radius,
                center_x + orbit_radius, center_y + orbit_radius,
                outline='#ff00ff', width=1, tags="boot", dash=(4, 4)
            )
            
            self.boot_canvas.create_oval(
                electron_x - 4, electron_y - 4,
                electron_x + 4, electron_y + 4,
                fill='#ffff00', outline='', tags="boot"
            )
        
        core_radius = 15
        pulse = math.sin(time.time() * 5) * 3 + core_radius
        self.boot_canvas.create_oval(
            center_x - pulse, center_y - pulse,
            center_x + pulse, center_y + pulse,
            fill='#00ffff', outline='', tags="boot"
        )
        
        self.boot_canvas.create_text(
            center_x, center_y + radius + 40,
            text="QUANTUM OS", font=('Arial', 16, 'bold'),
            fill='#00ffff', tags="boot"
        )
        
        self.boot_canvas.create_text(
            center_x, center_y + radius + 60,
            text="Created by Saleh Amoo", font=('Arial', 10),
            fill='#cccccc', tags="boot"
        )

    def draw_boot_progress(self):
        bar_width = 300
        bar_height = 12
        bar_x = (self.screen_width - bar_width) // 2
        bar_y = self.screen_height - 80
        
        self.boot_canvas.create_rectangle(
            bar_x, bar_y, bar_x + bar_width, bar_y + bar_height,
            outline='#333333', fill='#1a1a1a', width=2, tags="boot"
        )
        
        progress_width = (bar_width * self.boot_progress) // 100
        if progress_width > 0:
            self.boot_canvas.create_rectangle(
                bar_x, bar_y, bar_x + progress_width, bar_y + bar_height,
                fill='#00ffff', outline='', tags="boot"
            )
        
        self.boot_canvas.create_text(
            self.screen_width // 2, bar_y - 20,
            text=f"{self.boot_progress}%", font=('Arial', 12, 'bold'),
            fill='#00ffff', tags="boot"
        )
        
        status_messages = [
            (10, "Initializing Quantum Core..."),
            (25, "Loading Neural Networks..."),
            (40, "Establishing Quantum Entanglement..."),
            (55, "Calibrating Temporal Systems..."),
            (70, "Starting AI Processors..."),
            (85, "Loading User Interface..."),
            (95, "Finalizing System Checks..."),
            (100, "Ready!")
        ]
        
        current_status = "Booting Quantum Operating System..."
        for stage, message in status_messages:
            if self.boot_stage >= stage:
                current_status = message
        
        self.boot_canvas.create_text(
            self.screen_width // 2, bar_y - 50,
            text=current_status, font=('Arial', 10),
            fill='#00ff88', tags="boot"
        )

    def update_boot_sequence(self):
        if self.boot_stage < 100:
            increment = random.uniform(0.5, 2.0)
            self.boot_progress = min(100, self.boot_progress + increment)
            
            if self.boot_progress >= 10 and self.boot_stage < 10:
                self.boot_stage = 10
            elif self.boot_progress >= 25 and self.boot_stage < 25:
                self.boot_stage = 25
            elif self.boot_progress >= 40 and self.boot_stage < 40:
                self.boot_stage = 40
            elif self.boot_progress >= 55 and self.boot_stage < 55:
                self.boot_stage = 55
            elif self.boot_progress >= 70 and self.boot_stage < 70:
                self.boot_stage = 70
            elif self.boot_progress >= 85 and self.boot_stage < 85:
                self.boot_stage = 85
            elif self.boot_progress >= 95 and self.boot_stage < 95:
                self.boot_stage = 95
            elif self.boot_progress >= 100:
                self.boot_stage = 100

    def finish_boot_sequence(self):
        for alpha in range(100, -1, -5):
            self.boot_window.attributes('-alpha', alpha/100)
            self.boot_window.update()
            time.sleep(0.02)
        
        self.boot_window.destroy()
        self.root.deiconify()

    def launch_with_animation(self, signature):
        if self.animation_running:
            return
            
        self.animation_running = True
        
        self.q_cursor.execute('SELECT name FROM quantum_apps WHERE quantum_signature = ?', (signature,))
        result = self.q_cursor.fetchone()
        app_name = result[0] if result else "Quantum App"
        
        self.animation_overlay = tk.Frame(self.root, bg='#0a0a0a')
        self.animation_overlay.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.anim_canvas = tk.Canvas(self.animation_overlay, bg='#0a0a0a', 
                                   highlightthickness=0)
        self.anim_canvas.place(x=0, y=0, relwidth=1, relheight=1)
        
        self.quantum_transition_animation(app_name, signature, 0)

    def quantum_transition_animation(self, app_name, signature, frame):
        self.anim_canvas.delete("transition")
        
        center_x, center_y = self.screen_width // 2, self.screen_height // 2
        
        # انیمیشن جدید: حلقه‌های کوانتومی متحدالمرکز
        for i in range(8):
            radius = ((frame + i * 8) % 80) * 6
            alpha = max(0, 1 - radius / 480)
            color = f'#00{int(255 * alpha):02x}ff'
            
            self.anim_canvas.create_oval(
                center_x - radius, center_y - radius,
                center_x + radius, center_y + radius,
                outline=color, width=2, tags="transition"
            )
        
        # انیمیشن جدید: ذرات در حال چرخش
        particles_count = 12
        for i in range(particles_count):
            angle = (frame * 0.2 + i * 2 * math.pi / particles_count)
            distance = 80 + math.sin(frame * 0.1 + i) * 30
            x = center_x + distance * math.cos(angle)
            y = center_y + distance * math.sin(angle)
            
            particle_size = 3 + math.sin(frame * 0.15 + i) * 2
            color = ['#ff00ff', '#ffff00', '#00ff88'][i % 3]
            
            self.anim_canvas.create_oval(
                x - particle_size, y - particle_size,
                x + particle_size, y + particle_size,
                fill=color, outline='', tags="transition"
            )
            
            # خطوط اتصال
            next_i = (i + 1) % particles_count
            next_angle = (frame * 0.2 + next_i * 2 * math.pi / particles_count)
            next_distance = 80 + math.sin(frame * 0.1 + next_i) * 30
            next_x = center_x + next_distance * math.cos(next_angle)
            next_y = center_y + next_distance * math.sin(next_angle)
            
            line_alpha = 0.3 + math.sin(frame * 0.1 + i) * 0.2
            line_color = f'#ff44{int(255 * line_alpha):02x}'
            self.anim_canvas.create_line(
                x, y, next_x, next_y,
                fill=line_color, width=1, tags="transition"
            )
        
        # متن با افکت fade-in بهبود یافته
        alpha = min(1.0, frame / 25)
        text_color = f'#{"00"}{int(255 * alpha):02x}{"ff"}'
        
        # افکت سایه برای متن
        shadow_offset = 2
        self.anim_canvas.create_text(
            center_x + shadow_offset, center_y + shadow_offset,
            text=app_name, font=('Arial', 20, 'bold'),
            fill='#000033', tags="transition"
        )
        
        self.anim_canvas.create_text(
            center_x, center_y, text=app_name,
            font=('Arial', 20, 'bold'), fill=text_color,
            tags="transition"
        )
        
        # اضافه کردن افکت پالس
        if frame > 30:
            pulse_alpha = math.sin(frame * 0.3) * 0.3 + 0.7
            pulse_color = f'#ff44{int(255 * pulse_alpha):02x}'
            pulse_radius = 100 + math.sin(frame * 0.2) * 20
            
            self.anim_canvas.create_oval(
                center_x - pulse_radius, center_y - pulse_radius,
                center_x + pulse_radius, center_y + pulse_radius,
                outline=pulse_color, width=2, tags="transition"
            )
        
        if frame < 60:
            self.root.after(16, lambda: self.quantum_transition_animation(app_name, signature, frame + 1))
        else:
            self.animation_overlay.destroy()
            self.animation_running = False
            self.launch_quantum_app(signature)

    def launch_quantum_app(self, signature):
        app_launchers = {
            'QCOM001': QuantumPhone,
            'NMSG002': NeuralMessenger,
            'AVIS003': AICamera,
            'QBRO004': QuantumBrowser,
            'QCAL005': QuantumCalculator,
            'TCAL006': TemporalCalendar,
            'QAI007': QuantumAIAssistant,
            'NFIL008': NeuralFileSystem,
            'QMUS009': QuantumMusic,
            'NHLT010': NeuralHealth,
            'QFIN011': QuantumFinance,
            'SCTL012': SystemControl,
            'SHTD013': ShutdownScreen,
            'GAME014': NumberGuessingGame,
            'GAME015': TicTacToeGame
        }
        
        if signature in app_launchers:
            try:
                app_instance = app_launchers[signature](self)
                app_instance.show()
            except Exception as e:
                messagebox.showerror("Error", f"Could not launch app: {str(e)}")
        else:
            messagebox.showinfo("Quantum Os", f"Created by {signature}")

    def show_shutdown(self):
        """نمایش انیمیشن شات‌دان پیشرفته"""
        shutdown_window = ShutdownScreen(self)
        shutdown_window.show()

    def update_quantum_status(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        quantum_time = f"Q-TIME: {current_time}"
        self.quantum_time.config(text=quantum_time)
        
        self.system_metrics['quantum_coherence'] = 98.5 + random.uniform(-0.2, 0.2)
        self.system_metrics['neural_throughput'] = 450 + random.randint(-10, 10)
        self.system_metrics['temporal_stability'] = 99.8 + random.uniform(-0.1, 0.1)
        
        self.coherence_label.config(text=f"QC: {self.system_metrics['quantum_coherence']:.1f}%")
        self.throughput_label.config(text=f"NT: {self.system_metrics['neural_throughput']}")
        self.stability_label.config(text=f"TS: {self.system_metrics['temporal_stability']:.1f}%")
        
        self.root.after(1000, self.update_quantum_status)

    def start_quantum_services(self):
        threading.Thread(target=self.quantum_processing, daemon=True).start()
        threading.Thread(target=self.neural_learning, daemon=True).start()
        threading.Thread(target=self.widget_quantum_updates, daemon=True).start()

    def quantum_processing(self):
        while True:
            time.sleep(2)
            self.quantum_state = random.choice(["superposition", "entanglement", "coherence"])
            self.neural_activity = max(0.1, min(0.99, self.neural_activity + random.uniform(-0.05, 0.05)))

    def neural_learning(self):
        while True:
            time.sleep(5)

    def widget_quantum_updates(self):
        while True:
            for widget in self.neural_widgets:
                if hasattr(widget, 'quantum_update'):
                    try:
                        widget.quantum_update()
                    except:
                        pass
            time.sleep(3)

    def run(self):
        self.root.withdraw()
        self.show_boot_screen()
        
        try:
            self.root.mainloop()
        finally:
            if hasattr(self, 'quantum_db'):
                self.quantum_db.close()

# برنامه‌های کاربردی
class QuantumPhone(QuantumApp):
    def __init__(self, os):
        super().__init__(os)
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Quantum Phone")
        self.window.geometry("500x600")
        self.apply_theme()
        
        header = tk.Frame(self.window, bg='#1a1a1a', height=60)
        header.pack(fill='x')
        tk.Label(header, text="QUANTUM PHONE", font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='#00ffff').pack(expand=True)
        
        self.number_display = tk.Label(self.window, text="", font=('Arial', 20),
                                     bg='#1a1a1a', fg='white', width=15, height=2)
        self.number_display.pack(pady=10)
        
        keypad_frame = tk.Frame(self.window, bg='#0a0a0a')
        keypad_frame.pack(expand=True)
        
        keys = [
            '1', '2', '3',
            '4', '5', '6', 
            '7', '8', '9',
            '*', '0', '#'
        ]
        
        for i, key in enumerate(keys):
            row = i // 3
            col = i % 3
            
            btn = tk.Button(keypad_frame, text=key, font=('Arial', 16),
                          bg='#2a2a2a', fg='white', width=4, height=2,
                          command=lambda k=key: self.add_digit(k))
            btn.grid(row=row, column=col, padx=5, pady=5)
        
        action_frame = tk.Frame(self.window, bg='#0a0a0a')
        action_frame.pack(pady=10)
        
        call_btn = tk.Button(action_frame, text="CALL", font=('Arial', 12),
                           bg='#00aa00', fg='white', width=8,
                           command=self.make_call)
        call_btn.pack(side='left', padx=5)
        
        clear_btn = tk.Button(action_frame, text="CLEAR", font=('Arial', 12),
                            bg='#aa0000', fg='white', width=8,
                            command=self.clear_number)
        clear_btn.pack(side='left', padx=5)
        
    def add_digit(self, digit):
        current = self.number_display.cget("text")
        if current == "0":
            self.number_display.config(text=digit)
        else:
            self.number_display.config(text=current + digit)
        
    def clear_number(self):
        self.number_display.config(text="")
        
    def make_call(self):
        number = self.number_display.cget("text")
        if number:
            messagebox.showinfo("Quantum Call", f"Calling: {number}\n\nQuantum encryption: ACTIVE\nSignal strength: EXCELLENT")
        else:
            messagebox.showwarning("No Number", "Please enter a number first")

class NeuralMessenger(QuantumApp):
    def __init__(self, os):
        super().__init__(os)
        self.current_chat = None
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Neural Messenger")
        self.window.geometry("400x500")
        self.apply_theme()
        
        header = tk.Frame(self.window, bg='#1a1a1a', height=60)
        header.pack(fill='x')
        tk.Label(header, text="NEURAL MESSENGER", font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='#00ffff').pack(expand=True)
        
        contacts_frame = tk.Frame(self.window, bg='#0a0a0a')
        contacts_frame.pack(fill='both', expand=True)
        
        contacts = ["John Quantum", "Sarah Neural", "Mike Photon", "Lisa AI"]
        for name in contacts:
            contact_btn = tk.Button(contacts_frame, text=name, font=('Arial', 12),
                                  bg='#1a1a1a', fg='white', height=2,
                                  command=lambda n=name: self.open_chat(n))
            contact_btn.pack(fill='x', padx=10, pady=2)
    
    def open_chat(self, contact):
        chat_window = tk.Toplevel(self.window)
        chat_window.title(f"Chat with {contact}")
        chat_window.geometry("300x400")
        
        header = tk.Frame(chat_window, bg='#1a1a1a', height=50)
        header.pack(fill='x')
        tk.Label(header, text=contact, font=('Arial', 14, 'bold'),
                bg='#1a1a1a', fg='white').pack(expand=True)
        
        chat_display = scrolledtext.ScrolledText(chat_window, 
                                               bg='#0a0a0a', fg='white',
                                               font=('Arial', 10), wrap=tk.WORD)
        chat_display.pack(fill='both', expand=True, padx=10, pady=10)
        chat_display.config(state=tk.DISABLED)
        
        input_frame = tk.Frame(chat_window, bg='#0a0a0a')
        input_frame.pack(fill='x', padx=10, pady=5)
        
        message_entry = tk.Entry(input_frame, font=('Arial', 11),
                               bg='#2a2a2a', fg='white')
        message_entry.pack(side='left', fill='x', expand=True, ipady=4)
        
        def send_message():
            message = message_entry.get()
            if message.strip():
                current_time = datetime.now().strftime("%H:%M")
                chat_display.config(state=tk.NORMAL)
                chat_display.insert(tk.END, f"[{current_time}] You: {message}\n\n")
                chat_display.config(state=tk.DISABLED)
                chat_display.see(tk.END)
                message_entry.delete(0, tk.END)
                
                chat_display.config(state=tk.NORMAL)
                replies = [
                    "Interesting! Tell me more.",
                    "Quantum computing is the future!",
                    "I need to learn more about that."
                ]
                reply = random.choice(replies)
                chat_display.insert(tk.END, f"[{current_time}] {contact}: {reply}\n\n")
                chat_display.config(state=tk.DISABLED)
                chat_display.see(tk.END)
        
        message_entry.bind('<Return>', lambda e: send_message())
        
        send_btn = tk.Button(input_frame, text="SEND", font=('Arial', 9),
                           bg='#00aa00', fg='white', command=send_message)
        send_btn.pack(side='right', padx=(5, 0))

class AICamera(QuantumApp):
    def __init__(self, os):
        super().__init__(os)
        self.camera_active = False
        self.animation_id = None
        self.particles = []
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("AI Camera")
        self.window.geometry("400x600")
        self.apply_theme()
        
        header = tk.Frame(self.window, bg='#1a1a1a', height=60)
        header.pack(fill='x')
        tk.Label(header, text="QUANTUM AI CAMERA", font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='#00ffff').pack(expand=True)
        
        # Camera preview with animation
        self.preview_frame = tk.Frame(self.window, bg='#0a0a0a', height=300)
        self.preview_frame.pack(fill='x', pady=20)
        self.preview_frame.pack_propagate(False)
        
        self.canvas = tk.Canvas(self.preview_frame, bg='#0a0a0a', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Initialize camera animation
        self.init_camera_animation()
        
        # Camera info
        info_frame = tk.Frame(self.window, bg='#0a0a0a')
        info_frame.pack(fill='x', padx=20, pady=10)
        
        self.info_label = tk.Label(info_frame, 
                                 text="QUANTUM CAMERA READY\nAI Object Detection: ACTIVE\nNeural Processing: 95%",
                                 font=('Arial', 10), bg='#1a1a1a', fg='#00ff88',
                                 justify='center', height=4)
        self.info_label.pack(fill='x', padx=10, pady=10)
        
        # Camera controls
        controls_frame = tk.Frame(self.window, bg='#0a0a0a')
        controls_frame.pack(fill='x', padx=20, pady=10)
        
        # Top row
        top_row = tk.Frame(controls_frame, bg='#0a0a0a')
        top_row.pack(fill='x', pady=5)
        
        flash_btn = tk.Button(top_row, text="FLASH", font=('Arial', 10),
                            bg='#2a2a2a', fg='white', width=8,
                            command=self.toggle_flash)
        flash_btn.pack(side='left', padx=5)
        
        timer_btn = tk.Button(top_row, text="TIMER", font=('Arial', 10),
                            bg='#2a2a2a', fg='white', width=8,
                            command=self.set_timer)
        timer_btn.pack(side='left', padx=5)
        
        mode_btn = tk.Button(top_row, text="AI MODE", font=('Arial', 10),
                           bg='#2a2a2a', fg='white', width=8,
                           command=self.toggle_ai_mode)
        mode_btn.pack(side='left', padx=5)
        
        # Capture button (large and centered)
        capture_frame = tk.Frame(controls_frame, bg='#0a0a0a')
        capture_frame.pack(fill='x', pady=15)
        
        self.capture_btn = tk.Button(capture_frame, text="CAPTURE", font=('Arial', 14, 'bold'),
                                   bg='#00aa00', fg='white', width=15, height=2,
                                   command=self.capture_image)
        self.capture_btn.pack()
        
        # Bottom row
        bottom_row = tk.Frame(controls_frame, bg='#0a0a0a')
        bottom_row.pack(fill='x', pady=5)
        
        gallery_btn = tk.Button(bottom_row, text="GALLERY", font=('Arial', 10),
                              bg='#2a2a2a', fg='white', width=8,
                              command=self.open_gallery)
        gallery_btn.pack(side='left', padx=5)
        
        settings_btn = tk.Button(bottom_row, text="SETTINGS", font=('Arial', 10),
                               bg='#2a2a2a', fg='white', width=8,
                               command=self.show_settings)
        settings_btn.pack(side='left', padx=5)
        
        filter_btn = tk.Button(bottom_row, text="FILTERS", font=('Arial', 10),
                             bg='#2a2a2a', fg='white', width=8,
                             command=self.show_filters)
        filter_btn.pack(side='left', padx=5)
        
        # Start camera animation
        self.camera_active = True
        self.animate_camera()
    
    def init_camera_animation(self):
        # Create lens effect
        self.canvas.create_oval(50, 50, 250, 250, outline='#00ffff', width=3, tags="lens")
        self.canvas.create_oval(70, 70, 230, 230, outline='#ff44ff', width=2, tags="lens")
        
        # Create particles for animation
        self.particles = []
        for _ in range(20):
            particle = {
                'x': random.uniform(60, 240),
                'y': random.uniform(60, 240),
                'size': random.uniform(2, 6),
                'speed': random.uniform(0.5, 2),
                'color': random.choice(['#00ffff', '#ff44ff', '#ffff00', '#00ff88']),
                'direction': random.uniform(0, 2 * math.pi)
            }
            self.particles.append(particle)
    
    def animate_camera(self):
        if not self.camera_active:
            return
            
        self.canvas.delete("animation")
        
        # Animate lens
        time_factor = time.time()
        pulse = math.sin(time_factor * 3) * 5 + 10
        self.canvas.create_oval(100-pulse, 100-pulse, 200+pulse, 200+pulse, 
                              outline='#00ff88', width=1, tags="animation")
        
        # Animate particles
        for particle in self.particles:
            # Move particle
            particle['x'] += math.cos(particle['direction']) * particle['speed']
            particle['y'] += math.sin(particle['direction']) * particle['speed']
            
            # Bounce off boundaries
            if particle['x'] < 60 or particle['x'] > 240:
                particle['direction'] = math.pi - particle['direction']
            if particle['y'] < 60 or particle['y'] > 240:
                particle['direction'] = -particle['direction']
            
            # Draw particle
            self.canvas.create_oval(
                particle['x'] - particle['size'], particle['y'] - particle['size'],
                particle['x'] + particle['size'], particle['y'] + particle['size'],
                fill=particle['color'], outline='', tags="animation"
            )
        
        # Draw crosshair
        self.canvas.create_line(150, 130, 150, 170, fill='#ffffff', width=1, tags="animation")
        self.canvas.create_line(130, 150, 170, 150, fill='#ffffff', width=1, tags="animation")
        
        # Draw focus points
        for angle in range(0, 360, 45):
            rad = angle * math.pi / 180
            x1 = 150 + 40 * math.cos(rad)
            y1 = 150 + 40 * math.sin(rad)
            x2 = 150 + 50 * math.cos(rad)
            y2 = 150 + 50 * math.sin(rad)
            self.canvas.create_line(x1, y1, x2, y2, fill='#ff44ff', width=2, tags="animation")
        
        # Continue animation
        self.animation_id = self.window.after(50, self.animate_camera)
    
    def capture_image(self):
        # Flash effect
        self.canvas.create_rectangle(0, 0, 300, 300, fill='white', tags="flash")
        self.window.after(100, lambda: self.canvas.delete("flash"))
        
        # Capture animation
        self.animate_capture()
        
        # Show success message
        self.window.after(500, lambda: messagebox.showinfo(
            "Quantum Capture", 
            "Image captured with AI enhancement!\n\n"
            "Objects detected: 3\n"
            "Image quality: 98%\n"
            "Neural processing complete\n"
            "Quantum optimization applied"
        ))
    
    def animate_capture(self):
        # Create concentric circles for capture effect
        for i in range(5):
            radius = 20 + i * 15
            self.canvas.create_oval(
                150-radius, 150-radius, 150+radius, 150+radius,
                outline='#00ff88', width=2, tags="capture"
            )
        self.window.after(200, lambda: self.canvas.delete("capture"))
    
    def toggle_flash(self):
        messagebox.showinfo("Flash", "Quantum flash toggled\nPhoton amplification: ACTIVE")
    
    def set_timer(self):
        messagebox.showinfo("Timer", "Quantum timer set\nTemporal capture in 3 seconds")
    
    def toggle_ai_mode(self):
        messagebox.showinfo("AI Mode", "Neural network enhanced\nObject recognition: MAXIMUM\nScene optimization: AI")
    
    def open_gallery(self):
        messagebox.showinfo("Gallery", "Quantum gallery accessed\nNeural image sorting active")
    
    def show_settings(self):
        messagebox.showinfo("Camera Settings", 
                          "Quantum Camera Settings:\n\n"
                          "Resolution: 64MP Quantum\n"
                          "AI Enhancement: MAX\n"
                          "Object Detection: ON\n"
                          "Face Recognition: ON\n"
                          "Scene Optimization: AI\n"
                          "Neural Processing: 95%")
    
    def show_filters(self):
        filters = ["Quantum Filter", "Neural Enhance", "AI Art", "Photon Boost", "Temporal Blend"]
        messagebox.showinfo("Filters", f"AI Filters Available:\n\n" + "\n".join(filters))
    
    def __del__(self):
        self.camera_active = False
        if self.animation_id:
            self.window.after_cancel(self.animation_id)

class QuantumBrowser(QuantumApp):
    def __init__(self, os):
        super().__init__(os)
        self.history = []
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Quantum Browser")
        self.window.geometry("500x600")
        self.apply_theme()
        
        header = tk.Frame(self.window, bg='#1a1a1a', height=60)
        header.pack(fill='x')
        tk.Label(header, text="QUANTUM BROWSER", font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='#00ffff').pack(expand=True)
        
        # Address bar
        address_frame = tk.Frame(self.window, bg='#0a0a0a')
        address_frame.pack(fill='x', padx=10, pady=5)
        
        self.address_entry = tk.Entry(address_frame, font=('Arial', 11),
                                    bg='#2a2a2a', fg='white')
        self.address_entry.pack(side='left', fill='x', expand=True, ipady=4)
        self.address_entry.insert(0, "quantum://browser/home")
        
        go_btn = tk.Button(address_frame, text="GO", font=('Arial', 9),
                         bg='#00aa00', fg='white', command=self.navigate)
        go_btn.pack(side='right', padx=(5, 0))
        
        # Browser content
        content_frame = tk.Frame(self.window, bg='#0a0a0a')
        content_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        content_text = scrolledtext.ScrolledText(content_frame, 
                                               bg='#1a1a1a', fg='white',
                                               font=('Arial', 10), wrap=tk.WORD)
        content_text.pack(fill='both', expand=True)
        
        # Display default content
        default_content = """QUANTUM BROWSER v3.5

Welcome to the Quantum Web!

Featured Sites:
• quantum://news/latest
• quantum://social/network  
• quantum://ai/assistant
• quantum://games/arcade
• quantum://learning/academy

Quantum Features:
• Neural ad-blocking
• AI content optimization
• Quantum encryption
• Temporal caching

Enter a quantum address to begin browsing..."""
        
        content_text.insert(tk.END, default_content)
        content_text.config(state=tk.DISABLED)
        
        # Navigation buttons
        nav_frame = tk.Frame(self.window, bg='#0a0a0a')
        nav_frame.pack(fill='x', padx=10, pady=5)
        
        back_btn = tk.Button(nav_frame, text="BACK", font=('Arial', 9),
                           bg='#2a2a2a', fg='white', width=8)
        back_btn.pack(side='left', padx=2)
        
        forward_btn = tk.Button(nav_frame, text="FORWARD", font=('Arial', 9),
                              bg='#2a2a2a', fg='white', width=8)
        forward_btn.pack(side='left', padx=2)
        
        refresh_btn = tk.Button(nav_frame, text="REFRESH", font=('Arial', 9),
                              bg='#2a2a2a', fg='white', width=8,
                              command=self.refresh_page)
        refresh_btn.pack(side='left', padx=2)
        
        home_btn = tk.Button(nav_frame, text="HOME", font=('Arial', 9),
                           bg='#2a2a2a', fg='white', width=8,
                           command=self.go_home)
        home_btn.pack(side='left', padx=2)
    
    def navigate(self):
        url = self.address_entry.get()
        self.history.append(url)
        messagebox.showinfo("Navigation", f"Navigating to: {url}\n\nQuantum encryption active\nNeural loading optimized")
    
    def refresh_page(self):
        messagebox.showinfo("Refresh", "Page refreshed with quantum acceleration")
    
    def go_home(self):
        self.address_entry.delete(0, tk.END)
        self.address_entry.insert(0, "quantum://browser/home")
        messagebox.showinfo("Home", "Returned to quantum home page")

class QuantumCalculator(QuantumApp):
    def __init__(self, os):
        super().__init__(os)
        self.current_input = ""
        self.result = ""
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Quantum Calculator")
        self.window.geometry("400x500")
        self.apply_theme()
        
        header = tk.Frame(self.window, bg='#1a1a1a', height=60)
        header.pack(fill='x')
        tk.Label(header, text="QUANTUM CALCULATOR", font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='#00ffff').pack(expand=True)
        
        # Display
        display_frame = tk.Frame(self.window, bg='#0a0a0a')
        display_frame.pack(fill='x', padx=20, pady=10)
        
        self.display_var = tk.StringVar()
        display_entry = tk.Entry(display_frame, textvariable=self.display_var,
                               font=('Arial', 18), bg='#1a1a1a', fg='white',
                               justify='right', state='readonly')
        display_entry.pack(fill='x', ipady=10)
        
        # Keypad
        keypad_frame = tk.Frame(self.window, bg='#0a0a0a')
        keypad_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        buttons = [
            ('7', '8', '9', '/', 'C'),
            ('4', '5', '6', '*', '⌫'),
            ('1', '2', '3', '-', 'Q'),
            ('0', '.', '=', '+', 'π')
        ]
        
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                btn = tk.Button(keypad_frame, text=text, font=('Arial', 14),
                              bg='#2a2a2a', fg='white', width=5, height=2,
                              command=lambda t=text: self.button_click(t))
                btn.grid(row=i, column=j, padx=2, pady=2, sticky='nsew')
                keypad_frame.grid_columnconfigure(j, weight=1)
            keypad_frame.grid_rowconfigure(i, weight=1)
    
    def button_click(self, text):
        if text == 'C':
            self.current_input = ""
            self.result = ""
        elif text == '⌫':
            self.current_input = self.current_input[:-1]
        elif text == '=':
            try:
                self.result = str(eval(self.current_input))
                self.current_input = self.result
            except:
                self.result = "Error"
                self.current_input = ""
        elif text == 'Q':
            # Quantum calculation
            try:
                num = float(eval(self.current_input))
                quantum_result = num * random.uniform(0.99, 1.01)
                self.result = f"{quantum_result:.6f}"
                self.current_input = self.result
            except:
                self.result = "Q-Error"
                self.current_input = ""
        elif text == 'π':
            self.current_input += str(math.pi)
        else:
            self.current_input += text
        
        self.display_var.set(self.current_input if self.current_input else "0")

class TemporalCalendar(QuantumApp):
    def __init__(self, os):
        super().__init__(os)
        self.current_date = datetime.now()
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Temporal Calendar")
        self.window.geometry("500x600")
        self.apply_theme()
        
        header = tk.Frame(self.window, bg='#1a1a1a', height=60)
        header.pack(fill='x')
        tk.Label(header, text="TEMPORAL CALENDAR", font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='#00ffff').pack(expand=True)
        
        # Date navigation
        nav_frame = tk.Frame(self.window, bg='#0a0a0a')
        nav_frame.pack(fill='x', padx=20, pady=10)
        
        prev_btn = tk.Button(nav_frame, text="◀", font=('Arial', 14),
                           bg='#2a2a2a', fg='white', width=4,
                           command=self.previous_month)
        prev_btn.pack(side='left')
        
        self.month_label = tk.Label(nav_frame, text="", font=('Arial', 16, 'bold'),
                                  bg='#0a0a0a', fg='#00ff88')
        self.month_label.pack(side='left', expand=True)
        
        next_btn = tk.Button(nav_frame, text="▶", font=('Arial', 14),
                           bg='#2a2a2a', fg='white', width=4,
                           command=self.next_month)
        next_btn.pack(side='right')
        
        # Calendar grid
        self.calendar_frame = tk.Frame(self.window, bg='#0a0a0a')
        self.calendar_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.update_calendar()
        
        # Today button
        today_btn = tk.Button(self.window, text="TODAY", font=('Arial', 12),
                            bg='#00aa00', fg='white', command=self.go_today)
        today_btn.pack(pady=10)
    
    def update_calendar(self):
        # Clear existing calendar
        for widget in self.calendar_frame.winfo_children():
            widget.destroy()
        
        # Set month label
        self.month_label.config(text=self.current_date.strftime("%B %Y"))
        
        # Create day headers
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        for i, day in enumerate(days):
            label = tk.Label(self.calendar_frame, text=day, font=('Arial', 10, 'bold'),
                           bg='#1a1a1a', fg='#00ffff', width=10, height=2)
            label.grid(row=0, column=i, padx=1, pady=1, sticky='nsew')
        
        # Get first day of month and number of days
        year = self.current_date.year
        month = self.current_date.month
        first_day = datetime(year, month, 1)
        days_in_month = (datetime(year, month % 12 + 1, 1) - timedelta(days=1)).day if month < 12 else 31
        
        # Fill calendar
        row = 1
        col = first_day.weekday()
        
        for day in range(1, days_in_month + 1):
            is_today = (day == datetime.now().day and month == datetime.now().month and year == datetime.now().year)
            
            bg_color = '#00ff88' if is_today else '#2a2a2a'
            fg_color = '#000000' if is_today else 'white'
            
            day_btn = tk.Button(self.calendar_frame, text=str(day), font=('Arial', 10),
                              bg=bg_color, fg=fg_color, width=10, height=2,
                              command=lambda d=day: self.day_selected(d))
            day_btn.grid(row=row, column=col, padx=1, pady=1, sticky='nsew')
            
            col += 1
            if col > 6:
                col = 0
                row += 1
        
        # Configure grid weights
        for i in range(7):
            self.calendar_frame.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.calendar_frame.grid_rowconfigure(i + 1, weight=1)
    
    def previous_month(self):
        self.current_date = self.current_date.replace(day=1) - timedelta(days=1)
        self.current_date = self.current_date.replace(day=1)
        self.update_calendar()
    
    def next_month(self):
        if self.current_date.month == 12:
            self.current_date = self.current_date.replace(year=self.current_date.year + 1, month=1, day=1)
        else:
            self.current_date = self.current_date.replace(month=self.current_date.month + 1, day=1)
        self.update_calendar()
    
    def go_today(self):
        self.current_date = datetime.now()
        self.update_calendar()
    
    def day_selected(self, day):
        selected_date = self.current_date.replace(day=day)
        messagebox.showinfo("Date Selected", 
                          f"Selected: {selected_date.strftime('%B %d, %Y')}\n\n"
                          f"Quantum temporal analysis complete\n"
                          f"Time dilation factor: {random.uniform(0.999, 1.001):.6f}")

class QuantumAIAssistant(QuantumApp):
    def __init__(self, os):
        super().__init__(os)
        self.conversation = []
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Quantum AI Assistant")
        self.window.geometry("500x600")
        self.apply_theme()
        
        header = tk.Frame(self.window, bg='#1a1a1a', height=60)
        header.pack(fill='x')
        tk.Label(header, text="QUANTUM AI ASSISTANT", font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='#00ffff').pack(expand=True)
        
        # Conversation display
        self.chat_display = scrolledtext.ScrolledText(self.window, 
                                                    bg='#1a1a1a', fg='white',
                                                    font=('Arial', 10), wrap=tk.WORD)
        self.chat_display.pack(fill='both', expand=True, padx=20, pady=10)
        self.chat_display.config(state=tk.DISABLED)
        
        # Welcome message
        welcome_msg = "Quantum AI: Hello! I'm your quantum-powered assistant. How can I help you today?\n\n"
        self.add_message(welcome_msg)
        
        # Input area
        input_frame = tk.Frame(self.window, bg='#0a0a0a')
        input_frame.pack(fill='x', padx=20, pady=10)
        
        self.input_entry = tk.Entry(input_frame, font=('Arial', 11),
                                  bg='#2a2a2a', fg='white')
        self.input_entry.pack(side='left', fill='x', expand=True, ipady=4)
        self.input_entry.bind('<Return>', lambda e: self.send_message())
        
        send_btn = tk.Button(input_frame, text="SEND", font=('Arial', 9),
                           bg='#00aa00', fg='white', command=self.send_message)
        send_btn.pack(side='right', padx=(5, 0))
        
        # Quick actions
        actions_frame = tk.Frame(self.window, bg='#0a0a0a')
        actions_frame.pack(fill='x', padx=20, pady=5)
        
        quick_actions = ["Time", "Weather", "Calculate", "Joke", "Quantum"]
        for action in quick_actions:
            btn = tk.Button(actions_frame, text=action, font=('Arial', 8),
                          bg='#2a2a2a', fg='white', width=8,
                          command=lambda a=action: self.quick_action(a))
            btn.pack(side='left', padx=2)
    
    def add_message(self, message):
        self.chat_display.config(state=tk.NORMAL)
        self.chat_display.insert(tk.END, message)
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
    
    def send_message(self):
        message = self.input_entry.get().strip()
        if message:
            self.add_message(f"You: {message}\n")
            self.input_entry.delete(0, tk.END)
            
            # AI response
            response = self.get_ai_response(message)
            self.add_message(f"Quantum AI: {response}\n\n")
    
    def quick_action(self, action):
        responses = {
            "Time": f"Current quantum time: {datetime.now().strftime('%H:%M:%S')}\nTemporal stability: 99.9%",
            "Weather": "Quantum weather analysis: Conditions optimal\nTemperature: 23.7°C\nNeural forecast: Stable",
            "Calculate": f"Quantum computation: {random.uniform(1, 100):.6f}",
            "Joke": "Why don't quantum physicists use Windows?\nBecause they can't handle the uncertainty!",
            "Quantum": "Quantum systems: ONLINE\nNeural networks: ACTIVE\nAI processing: OPTIMAL"
        }
        
        self.add_message(f"You: {action}\n")
        self.add_message(f"Quantum AI: {responses.get(action, 'Processing...')}\n\n")
    
    def get_ai_response(self, message):
        responses = [
            "I'm processing your request with quantum algorithms...",
            "Neural networks are analyzing your query...",
            "Quantum computation complete. Here's my response:",
            "AI analysis suggests the following:",
            "Based on quantum probability, I recommend:"
        ]
        
        ai_responses = [
            "Quantum systems are operating optimally.",
            "The neural network has processed your request successfully.",
            "Temporal analysis shows favorable conditions.",
            "Quantum probability suggests positive outcomes.",
            "AI optimization complete. All systems nominal."
        ]
        
        return f"{random.choice(responses)}\n{random.choice(ai_responses)}"

class NeuralFileSystem(QuantumApp):
    def __init__(self, os):
        super().__init__(os)
        self.current_path = os.path.expanduser("~")
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Neural File System")
        self.window.geometry("600x500")
        self.apply_theme()
        
        header = tk.Frame(self.window, bg='#1a1a1a', height=60)
        header.pack(fill='x')
        tk.Label(header, text="NEURAL FILE SYSTEM", font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='#00ffff').pack(expand=True)
        
        # Path display
        path_frame = tk.Frame(self.window, bg='#0a0a0a')
        path_frame.pack(fill='x', padx=20, pady=5)
        
        self.path_label = tk.Label(path_frame, text=self.current_path, 
                                 font=('Arial', 10), bg='#0a0a0a', fg='#cccccc',
                                 anchor='w')
        self.path_label.pack(fill='x')
        
        # File list
        list_frame = tk.Frame(self.window, bg='#0a0a0a')
        list_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        # Create listbox with scrollbar
        self.file_listbox = tk.Listbox(list_frame, bg='#1a1a1a', fg='white',
                                     font=('Arial', 11), selectbackground='#00ff88')
        self.file_listbox.pack(side='left', fill='both', expand=True)
        
        scrollbar = tk.Scrollbar(list_frame, orient='vertical')
        scrollbar.pack(side='right', fill='y')
        
        self.file_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.file_listbox.yview)
        
        # Bind double-click event
        self.file_listbox.bind('<Double-Button-1>', self.on_item_double_click)
        
        # Buttons
        button_frame = tk.Frame(self.window, bg='#0a0a0a')
        button_frame.pack(fill='x', padx=20, pady=10)
        
        back_btn = tk.Button(button_frame, text="BACK", font=('Arial', 10),
                           bg='#2a2a2a', fg='white', width=10,
                           command=self.go_back)
        back_btn.pack(side='left', padx=5)
        
        home_btn = tk.Button(button_frame, text="HOME", font=('Arial', 10),
                           bg='#2a2a2a', fg='white', width=10,
                           command=self.go_home)
        home_btn.pack(side='left', padx=5)
        
        refresh_btn = tk.Button(button_frame, text="REFRESH", font=('Arial', 10),
                              bg='#2a2a2a', fg='white', width=10,
                              command=self.refresh_list)
        refresh_btn.pack(side='left', padx=5)
        
        info_btn = tk.Button(button_frame, text="INFO", font=('Arial', 10),
                           bg='#2a2a2a', fg='white', width=10,
                           command=self.show_info)
        info_btn.pack(side='left', padx=5)
        
        # Load initial directory
        self.refresh_list()
    
    def refresh_list(self):
        self.file_listbox.delete(0, tk.END)
        
        try:
            # Add parent directory
            if self.current_path != os.path.dirname(self.current_path):
                self.file_listbox.insert(tk.END, "../ (Parent Directory)")
            
            # List files and directories
            for item in os.listdir(self.current_path):
                full_path = os.path.join(self.current_path, item)
                if os.path.isdir(full_path):
                    self.file_listbox.insert(tk.END, f"{item}/ (Directory)")
                else:
                    size = os.path.getsize(full_path)
                    self.file_listbox.insert(tk.END, f"{item} ({size} bytes)")
                    
        except PermissionError:
            self.file_listbox.insert(tk.END, "Permission denied")
        
        self.path_label.config(text=self.current_path)
    
    def on_item_double_click(self, event):
        selection = self.file_listbox.curselection()
        if selection:
            item = self.file_listbox.get(selection[0])
            
            if item.startswith("../"):
                # Go to parent directory
                self.current_path = os.path.dirname(self.current_path)
                self.refresh_list()
            elif item.endswith("/ (Directory)"):
                # Enter directory
                dir_name = item[:-13]  # Remove " (Directory)" suffix
                self.current_path = os.path.join(self.current_path, dir_name)
                self.refresh_list()
            else:
                # File selected
                file_name = item.split(' (')[0]  # Get filename before size
                messagebox.showinfo("File Selected", 
                                  f"File: {file_name}\n\n"
                                  f"Neural analysis complete\n"
                                  f"Quantum encryption: ACTIVE\n"
                                  f"File integrity: 100%")
    
    def go_back(self):
        if self.current_path != os.path.dirname(self.current_path):
            self.current_path = os.path.dirname(self.current_path)
            self.refresh_list()
    
    def go_home(self):
        self.current_path = os.path.expanduser("~")
        self.refresh_list()
    
    def show_info(self):
        try:
            total, used, free = shutil.disk_usage(self.current_path)
            info = (f"Neural File System Info:\n\n"
                   f"Current Path: {self.current_path}\n"
                   f"Total Space: {total // (2**30)} GB\n"
                   f"Used Space: {used // (2**30)} GB\n"
                   f"Free Space: {free // (2**30)} GB\n\n"
                   f"Quantum Indexing: ACTIVE\n"
                   f"Neural Search: ENABLED")
            messagebox.showinfo("System Info", info)
        except:
            messagebox.showinfo("System Info", "Neural File System v3.3\nQuantum storage optimization active")

class QuantumMusic(QuantumApp):
    def __init__(self, os):
        super().__init__(os)
        self.playlist = [
            "Quantum Symphony - Neural Beats",
            "Temporal Waves - AI Composer", 
            "Photon Dance - Digital Orchestra",
            "Entanglement Melody - Quantum Strings",
            "Superposition Rhythm - Neural Drums"
        ]
        self.current_track = 0
        self.is_playing = False
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Quantum Music")
        self.window.geometry("400x500")
        self.apply_theme()
        
        header = tk.Frame(self.window, bg='#1a1a1a', height=60)
        header.pack(fill='x')
        tk.Label(header, text="QUANTUM MUSIC", font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='#00ffff').pack(expand=True)
        
        # Album art
        art_frame = tk.Frame(self.window, bg='#0a0a0a', height=200)
        art_frame.pack(fill='x', pady=20)
        art_frame.pack_propagate(False)
        
        art_label = tk.Label(art_frame, text="⚛\nQUANTUM\nWAVES⚛", 
                           font=('Arial', 20, 'bold'), bg='#1a1a1a', fg='#00ff88',
                           height=8)
        art_label.pack(expand=True, fill='both', padx=40, pady=20)
        
        # Track info
        self.track_label = tk.Label(self.window, text="", font=('Arial', 14, 'bold'),
                                  bg='#0a0a0a', fg='white')
        self.track_label.pack(pady=10)
        
        self.artist_label = tk.Label(self.window, text="Quantum AI Composer", 
                                   font=('Arial', 11), bg='#0a0a0a', fg='#cccccc')
        self.artist_label.pack()
        
        # Progress
        progress_frame = tk.Frame(self.window, bg='#0a0a0a')
        progress_frame.pack(fill='x', padx=40, pady=10)
        
        self.progress = tk.Scale(progress_frame, from_=0, to=100, 
                               orient='horizontal', showvalue=False,
                               bg='#0a0a0a', fg='#00ff88', 
                               troughcolor='#2a2a2a', sliderrelief='flat')
        self.progress.pack(fill='x')
        
        time_frame = tk.Frame(self.window, bg='#0a0a0a')
        time_frame.pack(fill='x', padx=40)
        
        tk.Label(time_frame, text="0:00", font=('Arial', 9), 
                bg='#0a0a0a', fg='#cccccc').pack(side='left')
        tk.Label(time_frame, text="3:45", font=('Arial', 9),
                bg='#0a0a0a', fg='#cccccc').pack(side='right')
        
        # Controls
        controls_frame = tk.Frame(self.window, bg='#0a0a0a')
        controls_frame.pack(fill='x', padx=40, pady=20)
        
        prev_btn = tk.Button(controls_frame, text="⏮", font=('Arial', 16),
                           bg='#2a2a2a', fg='white', width=4,
                           command=self.previous_track)
        prev_btn.pack(side='left', padx=5)
        
        self.play_btn = tk.Button(controls_frame, text="▶", font=('Arial', 16),
                                bg='#00aa00', fg='white', width=4,
                                command=self.toggle_play)
        self.play_btn.pack(side='left', padx=5)
        
        next_btn = tk.Button(controls_frame, text="⏭", font=('Arial', 16),
                           bg='#2a2a2a', fg='white', width=4,
                           command=self.next_track)
        next_btn.pack(side='left', padx=5)
        
        # Playlist
        playlist_frame = tk.Frame(self.window, bg='#0a0a0a')
        playlist_frame.pack(fill='both', expand=True, padx=40, pady=10)
        
        tk.Label(playlist_frame, text="QUANTUM PLAYLIST", font=('Arial', 12, 'bold'),
                bg='#0a0a0a', fg='#00ffff').pack()
        
        self.playlist_listbox = tk.Listbox(playlist_frame, bg='#1a1a1a', fg='white',
                                         font=('Arial', 9), height=4)
        self.playlist_listbox.pack(fill='both', expand=True)
        
        for track in self.playlist:
            self.playlist_listbox.insert(tk.END, track)
        
        # Initialize first track
        self.update_track_display()
    
    def update_track_display(self):
        if self.playlist:
            self.track_label.config(text=self.playlist[self.current_track])
            self.playlist_listbox.selection_clear(0, tk.END)
            self.playlist_listbox.selection_set(self.current_track)
            self.playlist_listbox.see(self.current_track)
    
    def toggle_play(self):
        self.is_playing = not self.is_playing
        if self.is_playing:
            self.play_btn.config(text="⏸", bg='#ffaa00')
            messagebox.showinfo("Quantum Music", "Now playing with quantum audio enhancement!")
        else:
            self.play_btn.config(text="▶", bg='#00aa00')
    
    def next_track(self):
        if self.playlist:
            self.current_track = (self.current_track + 1) % len(self.playlist)
            self.update_track_display()
            self.is_playing = True
            self.play_btn.config(text="⏸", bg='#ffaa00')
    
    def previous_track(self):
        if self.playlist:
            self.current_track = (self.current_track - 1) % len(self.playlist)
            self.update_track_display()
            self.is_playing = True
            self.play_btn.config(text="⏸", bg='#ffaa00')

class NeuralHealth(QuantumApp):
    def __init__(self, os):
        super().__init__(os)
        self.health_data = {
            'heart_rate': 72,
            'steps': 8432,
            'sleep': 7.2,
            'calories': 2150
        }
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Neural Health")
        self.window.geometry("400x500")
        self.apply_theme()
        
        header = tk.Frame(self.window, bg='#1a1a1a', height=60)
        header.pack(fill='x')
        tk.Label(header, text="NEURAL HEALTH", font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='#00ffff').pack(expand=True)
        
        # Health metrics
        metrics_frame = tk.Frame(self.window, bg='#0a0a0a')
        metrics_frame.pack(fill='x', padx=20, pady=20)
        
        # Heart Rate
        hr_frame = tk.Frame(metrics_frame, bg='#1a1a1a')
        hr_frame.pack(fill='x', pady=5)
        tk.Label(hr_frame, text="HEART RATE", font=('Arial', 12, 'bold'),
                bg='#1a1a1a', fg='#ff4444').pack(anchor='w')
        self.hr_label = tk.Label(hr_frame, text=f"{self.health_data['heart_rate']} BPM", 
                               font=('Arial', 18, 'bold'), bg='#1a1a1a', fg='white')
        self.hr_label.pack(anchor='w')
        
        # Steps
        steps_frame = tk.Frame(metrics_frame, bg='#1a1a1a')
        steps_frame.pack(fill='x', pady=5)
        tk.Label(steps_frame, text="DAILY STEPS", font=('Arial', 12, 'bold'),
                bg='#1a1a1a', fg='#00ff88').pack(anchor='w')
        self.steps_label = tk.Label(steps_frame, text=f"{self.health_data['steps']:,}", 
                                  font=('Arial', 18, 'bold'), bg='#1a1a1a', fg='white')
        self.steps_label.pack(anchor='w')
        
        # Sleep
        sleep_frame = tk.Frame(metrics_frame, bg='#1a1a1a')
        sleep_frame.pack(fill='x', pady=5)
        tk.Label(sleep_frame, text="SLEEP", font=('Arial', 12, 'bold'),
                bg='#1a1a1a', fg='#ff44ff').pack(anchor='w')
        self.sleep_label = tk.Label(sleep_frame, text=f"{self.health_data['sleep']} hours", 
                                  font=('Arial', 18, 'bold'), bg='#1a1a1a', fg='white')
        self.sleep_label.pack(anchor='w')
        
        # Calories
        calories_frame = tk.Frame(metrics_frame, bg='#1a1a1a')
        calories_frame.pack(fill='x', pady=5)
        tk.Label(calories_frame, text="CALORIES", font=('Arial', 12, 'bold'),
                bg='#1a1a1a', fg='#ffff00').pack(anchor='w')
        self.calories_label = tk.Label(calories_frame, text=f"{self.health_data['calories']} cal", 
                                     font=('Arial', 18, 'bold'), bg='#1a1a1a', fg='white')
        self.calories_label.pack(anchor='w')
        
        # Health status
        status_frame = tk.Frame(self.window, bg='#0a0a0a')
        status_frame.pack(fill='x', padx=20, pady=10)
        
        self.status_label = tk.Label(status_frame, text="HEALTH STATUS: OPTIMAL", 
                                   font=('Arial', 14, 'bold'), bg='#0a0a0a', fg='#00ff88')
        self.status_label.pack()
        
        # Recommendations
        recommend_frame = tk.Frame(self.window, bg='#1a1a1a')
        recommend_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        recommend_text = scrolledtext.ScrolledText(recommend_frame, 
                                                 bg='#1a1a1a', fg='white',
                                                 font=('Arial', 9), wrap=tk.WORD,
                                                 height=6)
        recommend_text.pack(fill='both', expand=True)
        
        recommendations = """Neural Health Recommendations:

• Continue current activity level
• Maintain hydration: 2.3L daily  
• Sleep quality: 92% (Excellent)
• Heart rate variability: Optimal
• Stress levels: Low

Quantum biometrics show all systems operating within optimal parameters."""
        
        recommend_text.insert(tk.END, recommendations)
        recommend_text.config(state=tk.DISABLED)
        
        # Update button
        update_btn = tk.Button(self.window, text="UPDATE METRICS", font=('Arial', 12),
                             bg='#00aa00', fg='white', command=self.update_metrics)
        update_btn.pack(pady=10)
    
    def update_metrics(self):
        # Simulate metric updates
        self.health_data['heart_rate'] = 70 + random.randint(-5, 5)
        self.health_data['steps'] = 8000 + random.randint(0, 1000)
        self.health_data['sleep'] = round(7.0 + random.uniform(-0.5, 0.5), 1)
        self.health_data['calories'] = 2100 + random.randint(-100, 100)
        
        self.hr_label.config(text=f"{self.health_data['heart_rate']} BPM")
        self.steps_label.config(text=f"{self.health_data['steps']:,}")
        self.sleep_label.config(text=f"{self.health_data['sleep']} hours")
        self.calories_label.config(text=f"{self.health_data['calories']} cal")
        
        messagebox.showinfo("Health Update", "Neural health metrics updated!\nQuantum biometric analysis complete.")

class QuantumFinance(QuantumApp):
    def __init__(self, os):
        super().__init__(os)
        self.portfolio = {
            'Quantum Stocks': 15420.50,
            'Neural Funds': 8920.75,
            'AI Investments': 12345.25,
            'Crypto Assets': 5678.90
        }
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Quantum Finance")
        self.window.geometry("500x500")
        self.apply_theme()
        
        header = tk.Frame(self.window, bg='#1a1a1a', height=60)
        header.pack(fill='x')
        tk.Label(header, text="QUANTUM FINANCE", font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='#00ffff').pack(expand=True)
        
        # Portfolio summary
        summary_frame = tk.Frame(self.window, bg='#0a0a0a')
        summary_frame.pack(fill='x', padx=20, pady=10)
        
        total = sum(self.portfolio.values())
        tk.Label(summary_frame, text="TOTAL PORTFOLIO", font=('Arial', 12, 'bold'),
                bg='#0a0a0a', fg='#cccccc').pack(anchor='w')
        self.total_label = tk.Label(summary_frame, text=f"${total:,.2f}", 
                                  font=('Arial', 20, 'bold'), bg='#0a0a0a', fg='#00ff88')
        self.total_label.pack(anchor='w')
        
        # Portfolio items
        portfolio_frame = tk.Frame(self.window, bg='#0a0a0a')
        portfolio_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        for asset, value in self.portfolio.items():
            asset_frame = tk.Frame(portfolio_frame, bg='#1a1a1a')
            asset_frame.pack(fill='x', pady=2)
            
            tk.Label(asset_frame, text=asset, font=('Arial', 11),
                   bg='#1a1a1a', fg='white').pack(side='left', padx=10)
            
            tk.Label(asset_frame, text=f"${value:,.2f}", font=('Arial', 11, 'bold'),
                   bg='#1a1a1a', fg='#00ff88').pack(side='right', padx=10)
        
        # Market data
        market_frame = tk.Frame(self.window, bg='#0a0a0a')
        market_frame.pack(fill='x', padx=20, pady=10)
        
        market_data = [
            ("QFI Index", "1,548.20", "+2.8%"),
            ("Neural Stocks", "845.75", "+1.2%"), 
            ("AI Funds", "1,234.50", "+3.1%"),
            ("Quantum Crypto", "45,678", "-0.5%")
        ]
        
        for name, value, change in market_data:
            market_row = tk.Frame(market_frame, bg='#1a1a1a')
            market_row.pack(fill='x', pady=1)
            
            tk.Label(market_row, text=name, font=('Arial', 9),
                   bg='#1a1a1a', fg='white').pack(side='left', padx=5)
            
            tk.Label(market_row, text=value, font=('Arial', 9),
                   bg='#1a1a1a', fg='#cccccc').pack(side='left', padx=5)
            
            color = '#00ff88' if '+' in change else '#ff4444'
            tk.Label(market_row, text=change, font=('Arial', 9, 'bold'),
                   bg='#1a1a1a', fg=color).pack(side='right', padx=5)
        
        # Actions
        action_frame = tk.Frame(self.window, bg='#0a0a0a')
        action_frame.pack(fill='x', padx=20, pady=10)
        
        trade_btn = tk.Button(action_frame, text="QUANTUM TRADE", font=('Arial', 11),
                            bg='#00aa00', fg='white', width=15,
                            command=self.quantum_trade)
        trade_btn.pack(side='left', padx=5)
        
        analyze_btn = tk.Button(action_frame, text="AI ANALYSIS", font=('Arial', 11),
                              bg='#2a2a2a', fg='white', width=15,
                              command=self.ai_analysis)
        analyze_btn.pack(side='left', padx=5)
    
    def quantum_trade(self):
        messagebox.showinfo("Quantum Trade", 
                          "Quantum trading algorithm activated!\n\n"
                          "Neural analysis complete\n"
                          "Market conditions: Favorable\n"
                          "Recommended action: HOLD\n"
                          "Quantum probability: 87.3%")
    
    def ai_analysis(self):
        analysis = ("AI Financial Analysis:\n\n"
                   "Portfolio Health: 94.2%\n"
                   "Risk Assessment: MEDIUM\n"
                   "Market Trend: BULLISH\n"
                   "Quantum Forecast: POSITIVE\n"
                   "Recommended: Diversify 15%")
        messagebox.showinfo("AI Analysis", analysis)

class SystemControl(QuantumApp):
    def __init__(self, os):
        super().__init__(os)
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("System Control")
        self.window.geometry("500x500")
        self.apply_theme()
        
        header = tk.Frame(self.window, bg='#1a1a1a', height=60)
        header.pack(fill='x')
        tk.Label(header, text="SYSTEM CONTROL", font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='#00ffff').pack(expand=True)
        
        # System status
        status_frame = tk.Frame(self.window, bg='#0a0a0a')
        status_frame.pack(fill='x', padx=20, pady=10)
        
        status_items = [
            ("Quantum Core", "ONLINE", '#00ff88'),
            ("Neural Network", "ACTIVE", '#00ff88'),
            ("AI Processor", "OPTIMAL", '#00ff88'),
            ("Temporal Sync", "STABLE", '#00ff88'),
            ("Security", "ENCRYPTED", '#00ff88'),
            ("Energy", "98%", '#ffff00')
        ]
        
        for name, status, color in status_items:
            status_row = tk.Frame(status_frame, bg='#1a1a1a')
            status_row.pack(fill='x', pady=2)
            
            tk.Label(status_row, text=name, font=('Arial', 11),
                   bg='#1a1a1a', fg='white').pack(side='left', padx=10)
            
            tk.Label(status_row, text=status, font=('Arial', 11, 'bold'),
                   bg='#1a1a1a', fg=color).pack(side='right', padx=10)
        
        # System controls
        controls_frame = tk.Frame(self.window, bg='#0a0a0a')
        controls_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        control_buttons = [
            ("OPTIMIZE SYSTEM", self.optimize_system, '#00aa00'),
            ("SECURITY SCAN", self.security_scan, '#ffaa00'),
            ("NEURAL UPDATE", self.neural_update, '#00ffff'),
            ("QUANTUM RESET", self.quantum_reset, '#ff4444'),
            ("BACKUP DATA", self.backup_data, '#ff44ff'),
            ("PERFORMANCE", self.performance_mode, '#ffff00')
        ]
        
        for i, (text, command, color) in enumerate(control_buttons):
            row = i // 2
            col = i % 2
            
            btn = tk.Button(controls_frame, text=text, font=('Arial', 10),
                          bg=color, fg='black' if color == '#ffff00' else 'white',
                          height=2, command=command)
            btn.grid(row=row, column=col, padx=5, pady=5, sticky='nsew')
            controls_frame.grid_columnconfigure(col, weight=1)
            controls_frame.grid_rowconfigure(row, weight=1)
        
        # System info
        info_frame = tk.Frame(self.window, bg='#0a0a0a')
        info_frame.pack(fill='x', padx=20, pady=10)
        
        info_text = """Quantum OS v4.0 - System Information
• Quantum Processor: 8.7 TQ/s
• Neural Capacity: 450 GQ/s  
• Memory: 98.3 GB available
• Storage: 1.2 TB quantum drive
• Security: Quantum encryption active"""
        
        info_label = tk.Label(info_frame, text=info_text, font=('Arial', 9),
                            bg='#0a0a0a', fg='#cccccc', justify='left')
        info_label.pack()
    
    def optimize_system(self):
        messagebox.showinfo("System Optimization", 
                          "Quantum optimization in progress...\n\n"
                          "Neural defragmentation: COMPLETE\n"
                          "Memory optimization: 99.8%\n"
                          "Quantum coherence: ENHANCED\n"
                          "System performance: +23.7%")
    
    def security_scan(self):
        messagebox.showinfo("Security Scan",
                          "Quantum security scan initiated...\n\n"
                          "Threat assessment: CLEAN\n"
                          "Encryption: 512-bit quantum\n"
                          "Firewall: ACTIVE\n"
                          "Neural protection: 100%")
    
    def neural_update(self):
        messagebox.showinfo("Neural Update",
                          "Downloading neural updates...\n\n"
                          "AI models: UPDATED\n"
                          "Quantum algorithms: OPTIMIZED\n"
                          "Security patches: APPLIED\n"
                          "System ready for reboot")
    
    def quantum_reset(self):
        messagebox.showinfo("Quantum Reset",
                          "Quantum system reset initiated...\n\n"
                          "Temporal synchronization: RESET\n"
                          "Neural networks: REBOOTING\n"
                          "Quantum state: REINITIALIZED\n"
                          "All systems nominal")
    
    def backup_data(self):
        messagebox.showinfo("Data Backup",
                          "Quantum backup in progress...\n\n"
                          "Neural data: SECURED\n"
                          "Quantum state: PRESERVED\n"
                          "Temporal snapshot: CREATED\n"
                          "Backup complete: 100%")
    
    def performance_mode(self):
        messagebox.showinfo("Performance Mode",
                          "Quantum performance mode activated!\n\n"
                          "Processing speed: +45.2%\n"
                          "Neural throughput: MAXIMUM\n"
                          "Energy consumption: OPTIMIZED\n"
                          "All systems at peak performance")

class NumberGuessingGame(QuantumApp):
    def __init__(self, os):
        super().__init__(os)
        self.secret_number = 0
        self.attempts = 0
        self.game_active = False
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Number Guessing Game")
        self.window.geometry("600x500")
        self.apply_theme()
        
        header = tk.Frame(self.window, bg='#1a1a1a', height=60)
        header.pack(fill='x')
        tk.Label(header, text="QUANTUM NUMBER GAME", font=('Arial', 14, 'bold'),
                bg='#1a1a1a', fg='#00ffff').pack(expand=True)
        
        # Game instructions
        instructions = tk.Label(self.window, 
                              text="I'm thinking of a number\nbetween 1 and 100!\n\nUse quantum intuition to guess!",
                              font=('Arial', 12), bg='#0a0a0a', fg='white',
                              justify='center')
        instructions.pack(pady=20)
        
        # Guess entry
        entry_frame = tk.Frame(self.window, bg='#0a0a0a')
        entry_frame.pack(pady=10)
        
        self.guess_entry = tk.Entry(entry_frame, font=('Arial', 14),
                                  bg='#2a2a2a', fg='white', width=10,
                                  justify='center')
        self.guess_entry.pack(padx=10, pady=5)
        
        # Feedback
        self.feedback_label = tk.Label(self.window, text="", font=('Arial', 11),
                                     bg='#0a0a0a', fg='#00ff88')
        self.feedback_label.pack(pady=5)
        
        # Attempts counter
        self.attempts_label = tk.Label(self.window, text="Attempts: 0", 
                                     font=('Arial', 10), bg='#0a0a0a', fg='#cccccc')
        self.attempts_label.pack()
        
        # Buttons
        button_frame = tk.Frame(self.window, bg='#0a0a0a')
        button_frame.pack(pady=20)
        
        guess_btn = tk.Button(button_frame, text="QUANTUM GUESS", font=('Arial', 12),
                            bg='#00aa00', fg='white', width=15,
                            command=self.check_guess)
        guess_btn.pack(pady=5)
        
        new_game_btn = tk.Button(button_frame, text="NEW GAME", font=('Arial', 12),
                               bg='#2a2a2a', fg='white', width=15,
                               command=self.new_game)
        new_game_btn.pack(pady=5)
        
        quantum_hint_btn = tk.Button(button_frame, text="QUANTUM HINT", font=('Arial', 10),
                                   bg='#ff44ff', fg='white', width=15,
                                   command=self.quantum_hint)
        quantum_hint_btn.pack(pady=5)
        
        # Start new game automatically
        self.new_game()
    
    def new_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.game_active = True
        self.guess_entry.delete(0, tk.END)
        self.feedback_label.config(text="Quantum number generated!\nGood luck!")
        self.attempts_label.config(text="Attempts: 0")
    
    def check_guess(self):
        if not self.game_active:
            return
            
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1
            self.attempts_label.config(text=f"Attempts: {self.attempts}")
            
            if guess < self.secret_number:
                self.feedback_label.config(text="Quantum reading: HIGHER\nThe number is greater!")
            elif guess > self.secret_number:
                self.feedback_label.config(text="Neural analysis: LOWER\nThe number is smaller!")
            else:
                self.feedback_label.config(text=f"QUANTUM SUCCESS!\nYou found it in {self.attempts} attempts!")
                self.game_active = False
                return
                
            self.guess_entry.delete(0, tk.END)
            
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number!")
    
    def quantum_hint(self):
        if not self.game_active:
            return
            
        hints = [
            f"The number is {'even' if self.secret_number % 2 == 0 else 'odd'}",
            f"The number is between {max(1, self.secret_number-10)} and {min(100, self.secret_number+10)}",
            f"Quantum probability suggests: {self.secret_number + random.randint(-5,5)}",
            f"Neural analysis: The number ends with {self.secret_number % 10}"
        ]
        
        self.feedback_label.config(text=f"Quantum Hint:\n{random.choice(hints)}")

class TicTacToeGame(QuantumApp):
    def __init__(self, os):
        super().__init__(os)
        self.board = ['' for _ in range(9)]
        self.current_player = 'X'
        self.game_active = True
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Tic Tac Toe")
        self.window.geometry("600x600")
        self.apply_theme()
        
        header = tk.Frame(self.window, bg='#1a1a1a', height=60)
        header.pack(fill='x')
        tk.Label(header, text="QUANTUM TIC TAC TOE", font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='#00ffff').pack(expand=True)
        
        # Current player display
        self.player_label = tk.Label(self.window, text="Player X's Turn", 
                                   font=('Arial', 14, 'bold'), bg='#0a0a0a', fg='#00ff88')
        self.player_label.pack(pady=10)
        
        # Game board
        board_frame = tk.Frame(self.window, bg='#0a0a0a')
        board_frame.pack(pady=10)
        
        self.buttons = []
        for i in range(9):
            row = i // 3
            col = i % 3
            
            btn = tk.Button(board_frame, text='', font=('Arial', 20, 'bold'),
                          bg='#2a2a2a', fg='white', width=4, height=2,
                          command=lambda idx=i: self.make_move(idx))
            btn.grid(row=row, column=col, padx=2, pady=2)
            self.buttons.append(btn)
        
        # Status
        self.status_label = tk.Label(self.window, text="Quantum game initialized!", 
                                   font=('Arial', 11), bg='#0a0a0a', fg='#cccccc')
        self.status_label.pack(pady=5)
        
        # Controls
        control_frame = tk.Frame(self.window, bg='#0a0a0a')
        control_frame.pack(pady=20)
        
        new_game_btn = tk.Button(control_frame, text="NEW GAME", font=('Arial', 12),
                               bg='#00aa00', fg='white', width=12,
                               command=self.new_game)
        new_game_btn.pack(side='left', padx=5)
        
        ai_move_btn = tk.Button(control_frame, text="AI MOVE", font=('Arial', 12),
                              bg='#ff44ff', fg='white', width=12,
                              command=self.ai_move)
        ai_move_btn.pack(side='left', padx=5)
        
        # دکمه انیمیشن جدید
        animation_btn = tk.Button(control_frame, text="CREATED BY SALEH", font=('Arial', 12),
                                bg='#ffff00', fg='black', width=15,
                                command=self.show_creator_animation)
        animation_btn.pack(side='left', padx=5)
    
    def new_game(self):
        self.board = ['' for _ in range(9)]
        self.current_player = 'X'
        self.game_active = True
        
        for btn in self.buttons:
            btn.config(text='', bg='#2a2a2a')
        
        self.player_label.config(text="Player X's Turn", fg='#00ff88')
        self.status_label.config(text="Quantum game started! Good luck!")
    
    def make_move(self, position):
        if not self.game_active or self.board[position] != '':
            return
            
        self.board[position] = self.current_player
        self.buttons[position].config(text=self.current_player, 
                                    bg='#00aa00' if self.current_player == 'X' else '#ff4444')
        
        if self.check_winner():
            self.player_label.config(text=f"Player {self.current_player} Wins!", fg='#ffff00')
            self.status_label.config(text="Quantum victory achieved!")
            self.game_active = False
            return
        elif '' not in self.board:
            self.player_label.config(text="It's a Draw!", fg='#ff44ff')
            self.status_label.config(text="Quantum stalemate detected!")
            self.game_active = False
            return
        
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.player_label.config(text=f"Player {self.current_player}'s Turn",
                               fg='#00ff88' if self.current_player == 'X' else '#ff4444')
    
    def ai_move(self):
        if not self.game_active or self.current_player != 'O':
            return
            
        # Simple AI - find first empty spot
        empty_spots = [i for i, spot in enumerate(self.board) if spot == '']
        if empty_spots:
            ai_choice = random.choice(empty_spots)
            self.make_move(ai_choice)
    
    def check_winner(self):
        # Check rows, columns, and diagonals
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != '':
                # Highlight winning combination
                for pos in combo:
                    self.buttons[pos].config(bg='#ffff00')
                return True
        return False

    def show_creator_animation(self):
        """انیمیشن ویژه برای نمایش سازنده"""
        animation_window = tk.Toplevel(self.window)
        animation_window.title("Created by Saleh Amoo")
        animation_window.geometry("400x300")
        animation_window.configure(bg='#000000')
        animation_window.overrideredirect(True)
        
        # قرار دادن پنجره در مرکز
        animation_window.geometry(f"+{animation_window.winfo_screenwidth()//2 - 200}+{animation_window.winfo_screenheight()//2 - 150}")
        
        canvas = tk.Canvas(animation_window, bg='#000000', width=400, height=300, highlightthickness=0)
        canvas.pack(fill='both', expand=True)
        
        def animate(frame=0):
            canvas.delete("all")
            
            # پس‌زمینه متحرک
            for i in range(20):
                x = (frame * 2 + i * 20) % 440 - 20
                y = 150 + math.sin(frame * 0.1 + i) * 50
                size = 5 + math.sin(frame * 0.05 + i) * 3
                color = ['#00ffff', '#ff44ff', '#ffff00', '#00ff88'][i % 4]
                canvas.create_oval(x-size, y-size, x+size, y+size, fill=color, outline='')
            
            # متن اصلی
            text_alpha = min(1.0, frame / 30)
            text_color = f'#{"00"}{int(255 * text_alpha):02x}{"ff"}'
            
            canvas.create_text(200, 100, text="CREATED BY", font=('Arial', 20, 'bold'), 
                             fill=text_color, tags="text")
            
            canvas.create_text(200, 140, text="SALEH AMOO", font=('Arial', 24, 'bold'), 
                             fill='#ffff00', tags="text")
            
            # افکت‌های ویژه
            if frame > 20:
                for i in range(8):
                    angle = (frame * 0.2 + i * 45) * math.pi / 180
                    radius = 80 + math.sin(frame * 0.1) * 20
                    x1 = 200 + radius * math.cos(angle)
                    y1 = 140 + radius * math.sin(angle)
                    x2 = 200 + (radius + 30) * math.cos(angle)
                    y2 = 140 + (radius + 30) * math.sin(angle)
                    canvas.create_line(x1, y1, x2, y2, fill='#ff44ff', width=3)
            
            # ذرات درخشان
            for i in range(15):
                part_x = 200 + math.cos(frame * 0.05 + i) * 100
                part_y = 140 + math.sin(frame * 0.05 + i) * 100
                part_size = 2 + math.sin(frame * 0.1 + i) * 2
                canvas.create_oval(part_x-part_size, part_y-part_size, 
                                 part_x+part_size, part_y+part_size, 
                                 fill='#00ff88', outline='')
            
            if frame < 100:
                animation_window.after(30, lambda: animate(frame + 1))
            else:
                animation_window.destroy()
        
        animate()

class ShutdownScreen:
    """انیمیشن شات‌دان پیشرفته"""
    def __init__(self, os):
        self.os = os
        self.window = None
        self.animation_stage = 0
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Quantum OS - Shutdown")
        self.window.geometry(f"{self.os.screen_width}x{self.os.screen_height}")
        self.window.configure(bg='#000000')
        self.window.overrideredirect(True)
        
        self.window.geometry(f"+{self.window.winfo_screenwidth()//2 - self.os.screen_width//2}+{self.window.winfo_screenheight()//2 - self.os.screen_height//2}")
        
        self.canvas = tk.Canvas(self.window, bg='#000000', 
                              width=self.os.screen_width, height=self.os.screen_height,
                              highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)
        
        self.animate_shutdown()

    def animate_shutdown(self):
        self.canvas.delete("shutdown")
        
        center_x, center_y = self.os.screen_width // 2, self.os.screen_height // 2
        
        # انیمیشن جدید: موج‌های کوانتومی در حال فروپاشی
        if self.animation_stage < 40:
            # موج‌های در حال جمع شدن
            for i in range(5):
                wave_radius = 100 - self.animation_stage * 2 + i * 20
                if wave_radius > 0:
                    alpha = max(0, 1 - self.animation_stage / 40)
                    color = f'#ff{int(255 * alpha):02x}44'
                    self.canvas.create_oval(
                        center_x - wave_radius, center_y - wave_radius,
                        center_x + wave_radius, center_y + wave_radius,
                        outline=color, width=2, tags="shutdown"
                    )
            
            # ذرات در حال فرار
            for i in range(15):
                angle = random.uniform(0, math.pi * 2)
                distance = 50 + self.animation_stage * 3
                x = center_x + distance * math.cos(angle)
                y = center_y + distance * math.sin(angle)
                
                particle_size = random.uniform(2, 5)
                color = random.choice(['#ff4444', '#ff8844', '#ffaa44'])
                
                self.canvas.create_oval(
                    x - particle_size, y - particle_size,
                    x + particle_size, y + particle_size,
                    fill=color, outline='', tags="shutdown"
                )
        
        elif self.animation_stage < 80:
            # مرحله فروپاشی هسته
            collapse_radius = max(10, 50 - (self.animation_stage - 40))
            pulse = math.sin(self.animation_stage * 0.3) * 5
            
            # هسته در حال فروپاشی
            self.canvas.create_oval(
                center_x - collapse_radius - pulse, center_y - collapse_radius - pulse,
                center_x + collapse_radius + pulse, center_y + collapse_radius + pulse,
                fill='#ff4444', outline='', tags="shutdown"
            )
            
            # ترک‌های انرژی
            for i in range(8):
                angle = i * 45 * math.pi / 180
                crack_length = (self.animation_stage - 40) * 2
                x1 = center_x + collapse_radius * math.cos(angle)
                y1 = center_y + collapse_radius * math.sin(angle)
                x2 = center_x + (collapse_radius + crack_length) * math.cos(angle)
                y2 = center_y + (collapse_radius + crack_length) * math.sin(angle)
                
                self.canvas.create_line(x1, y1, x2, y2, 
                                      fill='#ffff44', width=2, tags="shutdown")
        
        else:
            # مرحله نهایی - سیاه شدن
            fade_alpha = min(1.0, (self.animation_stage - 80) / 20)
            fade_color = f'#000000'
            
            self.canvas.create_rectangle(0, 0, self.os.screen_width, self.os.screen_height,
                                       fill=fade_color, outline='', tags="shutdown")
            
            # متن پایانی
            if self.animation_stage < 100:
                text_alpha = 1.0 - (self.animation_stage - 80) / 20
                text_color = f'#ff{int(255 * text_alpha):02x}44'
                
                self.canvas.create_text(center_x, center_y - 30,
                                      text="QUANTUM OS", font=('Arial', 16, 'bold'),
                                      fill=text_color, tags="shutdown")
                
                self.canvas.create_text(center_x, center_y,
                                      text="SYSTEM SHUTDOWN", font=('Arial', 12),
                                      fill=text_color, tags="shutdown")
                
                self.canvas.create_text(center_x, center_y + 30,
                                      text="Created by Saleh Amoo", font=('Arial', 10),
                                      fill=text_color, tags="shutdown")
        
        if self.animation_stage < 100:
            self.animation_stage += 1
            self.window.after(30, self.animate_shutdown)
        else:
            self.window.after(1000, self.final_shutdown)

    def final_shutdown(self):
        """پایان انیمیشن و خروج"""
        self.window.destroy()
        self.os.root.quit()

# Import needed for calendar
from datetime import timedelta

if __name__ == "__main__":
    print("QUANTUM OS v4.0 - Created by Saleh Amoo")
    print("Initializing quantum systems...")
    
    quantum_os = QuantumMobileOS()
    quantum_os.run()