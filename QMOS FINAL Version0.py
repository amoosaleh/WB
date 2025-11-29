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

# ابتدا تمام کلاس‌های پایه را تعریف می‌کنیم
class NeuralCache:
    """Quantum neural cache system"""
    def __init__(self):
        self.patterns = {}
        self.activation_levels = {}
        
    def store_pattern(self, pattern, activation):
        self.patterns[pattern] = activation
        
    def get_activation(self, pattern):
        return self.patterns.get(pattern, 0.0)

class QuantumAIProcessor:
    """Quantum AI processing unit"""
    def __init__(self):
        self.quantum_memory = []
        self.neural_weights = {}
        
    def process_quantum_query(self, query):
        """Process query with quantum AI"""
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
        """Perform quantum computation"""
        numbers = [random.uniform(1, 100) for _ in range(3)]
        result = sum(numbers) * random.uniform(0.99, 1.01)
        return f"Quantum computation result: {result:.6f}"

# Quantum Widgets
class QuantumWidget:
    """Base quantum widget class"""
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
        """Quantum state update"""
        self.quantum_state = (self.quantum_state + 0.1) % 1.0

class NeuralWeatherWidget(QuantumWidget):
    """Neural network weather prediction"""
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
        # Neural weather prediction updates
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

# حالا کلاس اصلی سیستم عامل
class QuantumMobileOS:
    def __init__(self):
        # Quantum system settings
        self.quantum_state = "superposition"
        self.neural_activity = 0.85
        self.quantum_entanglement = 0.92
        
        # Mobile specifications
        self.screen_width = 360
        self.screen_height = 740
        self.dpi = 440
        
        # Create main window
        self.root = tk.Tk()
        self.root.title("Quantum OS v3.0 - Neural Interface")
        self.root.geometry(f"{self.screen_width}x{self.screen_height}")
        self.root.configure(bg='#0a0a0a')
        self.root.resizable(False, False)
        
        # Hide main window initially
        self.root.withdraw()
        
        # Animation system
        self.animation_running = False
        
        # File system
        self.current_directory = os.path.expanduser("~")  # Start from home directory
        
        # Initialize quantum systems
        self.setup_quantum_core()
        self.setup_neural_interface()
        self.start_quantum_services()

        # اضافه کردن ویژگی‌های جدید
        self.setup_enhanced_features()

    def setup_enhanced_features(self):
        """راه‌اندازی ویژگی‌های پیشرفته جدید"""
        # مدیر تم
        self.themes = {
            'quantum': {'bg': '#0a0a0a', 'fg': '#00ffff', 'accent': '#ff44ff'},
            'dark': {'bg': '#1a1a1a', 'fg': '#ffffff', 'accent': '#ff8800'},
            'blue': {'bg': '#001122', 'fg': '#00ffff', 'accent': '#ff4444'},
            'purple': {'bg': '#110011', 'fg': '#ff44ff', 'accent': '#00ffff'},
            'green': {'bg': '#001100', 'fg': '#00ff88', 'accent': '#ff44ff'}
        }
        self.current_theme = 'quantum'

    def setup_quantum_core(self):
        """Quantum computing core system"""
        self.quantum_settings = {
            'quantum_processing': True,
            'neural_networks': True,
            'holographic_display': False,
            'temporal_sync': True,
            'quantum_encryption': True
        }
        
        # Quantum database
        self.setup_quantum_database()
        
        # Neural cache
        self.neural_cache = NeuralCache()
        
        # Quantum AI
        self.quantum_ai = QuantumAIProcessor()
        
        # System metrics
        self.system_metrics = {
            'quantum_coherence': 98.7,
            'neural_throughput': 450,
            'temporal_stability': 99.9,
            'quantum_efficiency': 87.3
        }

    def setup_quantum_database(self):
        """Quantum-entangled database"""
        self.quantum_db = sqlite3.connect(':memory:', check_same_thread=False)
        self.q_cursor = self.quantum_db.cursor()
        
        # Quantum apps table
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
        
        # Contacts table
        self.q_cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY,
                name TEXT,
                number TEXT,
                email TEXT
            )
        ''')
        
        # Messages table
        self.q_cursor.execute('''
            CREATE TABLE IF NOT EXISTS messages (
                id INTEGER PRIMARY KEY,
                contact TEXT,
                message TEXT,
                timestamp TEXT,
                is_sent BOOLEAN
            )
        ''')
        
        # Files table for tracking
        self.q_cursor.execute('''
            CREATE TABLE IF NOT EXISTS file_history (
                id INTEGER PRIMARY KEY,
                filename TEXT,
                path TEXT,
                file_type TEXT,
                size INTEGER,
                last_accessed TEXT
            )
        ''')
        
        self.initialize_quantum_data()

    def initialize_quantum_data(self):
        """Initialize quantum system data"""
        quantum_apps = [
            ('Quantum Phone', 'QCOM001', 0.95, 3, '4.2'),
            ('Neural Messenger', 'NMSG002', 0.92, 2, '3.8'),
            ('AI Camera', 'AVIS003', 0.98, 4, '5.1'),
            ('Quantum Browser', 'QBRO004', 0.89, 2, '3.5'),
            ('Quantum Calculator', 'QCAL005', 0.94, 3, '4.0'),
            ('Temporal Calendar', 'TCAL006', 0.97, 4, '4.8'),
            ('Quantum AI', 'QAI007', 0.96, 3, '4.1'),
            ('Neural Files', 'NFIL008', 0.91, 2, '3.3'),
            ('Quantum Music', 'QMUS009', 0.93, 3, '4.2'),
            ('Neural Health', 'NHLT010', 0.90, 2, '3.0'),
            ('Quantum Finance', 'QFIN011', 0.88, 2, '2.8'),
            ('System Control', 'SCTL012', 0.99, 5, '6.0'),
            ('Shutdown', 'SHTD013', 0.99, 1, '1.0'),
            # اضافه کردن برنامه‌های جدید
            ('Number Game', 'GAME014', 0.85, 1, '2.0'),
            ('Tic Tac Toe', 'GAME015', 0.88, 1, '2.1')
        ]
        
        for app in quantum_apps:
            self.q_cursor.execute('''
                INSERT INTO quantum_apps (name, quantum_signature, neural_compatibility, processing_tier, version)
                VALUES (?, ?, ?, ?, ?)
            ''', app)
        
        # Sample contacts
        contacts = [
            ('John Quantum', '+1-555-0101', 'john@quantum.com'),
            ('Sarah Neural', '+1-555-0102', 'sarah@neural.com'),
            ('Mike Photon', '+1-555-0103', 'mike@photon.com'),
            ('Lisa AI', '+1-555-0104', 'lisa@ai.com')
        ]
        
        for contact in contacts:
            self.q_cursor.execute('''
                INSERT INTO contacts (name, number, email)
                VALUES (?, ?, ?)
            ''', contact)
        
        # Sample messages
        messages = [
            ('John Quantum', 'Hello! How are you?', '10:30 AM', False),
            ('Sarah Neural', 'Meeting at 2 PM', '09:15 AM', False),
            ('Mike Photon', 'Quantum data received', 'Yesterday', False)
        ]
        
        for msg in messages:
            self.q_cursor.execute('''
                INSERT INTO messages (contact, message, timestamp, is_sent)
                VALUES (?, ?, ?, ?)
            ''', msg)
        
        self.quantum_db.commit()

    def setup_neural_interface(self):
        """Advanced neural interface"""
        # Quantum status bar
        self.setup_quantum_status()
        
        # Main interface
        self.setup_quantum_interface()
        
        # Neural navigation
        self.setup_neural_navigation()

    def setup_quantum_status(self):
        """Quantum-enhanced status bar"""
        self.status_frame = tk.Frame(self.root, bg='#0f0f0f', height=35)
        self.status_frame.pack(fill='x')
        self.status_frame.pack_propagate(False)
        
        # Quantum time display
        self.quantum_time = tk.Label(self.status_frame, text="", 
                                   font=('Arial', 9, 'bold'),
                                   bg='#0f0f0f', fg='#00ffff')
        self.quantum_time.pack(side='left', padx=12)
        
        # Quantum metrics
        metrics_frame = tk.Frame(self.status_frame, bg='#0f0f0f')
        metrics_frame.pack(side='right', padx=12)
        
        self.coherence_label = tk.Label(self.status_frame, text="QC: 98.7%", font=('Arial', 8),
                        bg='#0f0f0f', fg='#00ff88')
        self.coherence_label.pack(side='right', padx=4)
        
        self.throughput_label = tk.Label(self.status_frame, text="NT: 450", font=('Arial', 8),
                        bg='#0f0f0f', fg='#ff44ff')
        self.throughput_label.pack(side='right', padx=4)
        
        self.stability_label = tk.Label(self.status_frame, text="TS: 99.9%", font=('Arial', 8),
                        bg='#0f0f0f', fg='#ffff00')
        self.stability_label.pack(side='right', padx=4)
        
        # اضافه کردن دکمه تغییر تم
        self.theme_btn = tk.Button(self.status_frame, text="THEME", font=('Arial', 7),
                                 bg='#252525', fg='#ff44ff', command=self.change_theme)
        self.theme_btn.pack(side='right', padx=4)
        
        self.update_quantum_status()

    def setup_quantum_interface(self):
        """Main quantum interface"""
        self.main_frame = tk.Frame(self.root, bg='#0a0a0a')
        self.main_frame.pack(fill='both', expand=True)
        
        # Quantum visualization
        self.setup_quantum_visualization()
        
        # Neural widgets
        self.setup_neural_widgets()
        
        # Quantum app grid
        self.setup_quantum_apps()

    def setup_quantum_visualization(self):
        """Real-time quantum state visualization"""
        self.quantum_canvas = tk.Canvas(self.main_frame, bg='#0a0a0a', 
                                       height=180, highlightthickness=0)
        self.quantum_canvas.pack(fill='x', pady=(10, 5))
        
        # Quantum particles
        self.quantum_particles = []
        self.wave_functions = []
        
        self.initialize_quantum_field()
        self.animate_quantum_field()

    def initialize_quantum_field(self):
        """Initialize quantum field particles"""
        # Create quantum particles
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
        
        # Create wave functions
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
        """Get quantum-inspired color"""
        colors = ['#00ffff', '#ff00ff', '#ffff00', '#00ff88', '#ff4444', '#8888ff']
        return random.choice(colors)

    def animate_quantum_field(self):
        """Animate quantum field in real-time"""
        if hasattr(self, 'quantum_canvas'):
            self.quantum_canvas.delete("quantum")
            
            # Draw wave functions
            for wave in self.wave_functions:
                points = []
                for x in range(0, 361, 5):
                    y = 90 + wave['amplitude'] * math.sin(wave['frequency'] * x + wave['phase'])
                    points.extend([x, y])
                
                self.quantum_canvas.create_line(points, fill=wave['color'], 
                                              width=1.5, tags="quantum", smooth=True)
                wave['phase'] += 0.1
            
            # Draw quantum particles
            for particle in self.quantum_particles:
                # Update position with quantum uncertainty
                particle['x'] += particle['vx'] + random.uniform(-0.3, 0.3)
                particle['y'] += particle['vy'] + random.uniform(-0.3, 0.3)
                
                # Quantum tunneling effect
                if random.random() < 0.02:
                    particle['x'] = random.uniform(50, 310)
                    particle['y'] = random.uniform(30, 150)
                
                # Boundary conditions with quantum reflection
                if particle['x'] < 20 or particle['x'] > 340:
                    particle['vx'] *= -1
                    particle['color'] = self.get_quantum_color()
                if particle['y'] < 20 or particle['y'] > 160:
                    particle['vy'] *= -1
                    particle['color'] = self.get_quantum_color()
                
                # Draw particle with energy-based size
                size = 2 + particle['energy']
                self.quantum_canvas.create_oval(
                    particle['x'] - size, particle['y'] - size,
                    particle['x'] + size, particle['y'] + size,
                    fill=particle['color'], outline='', tags="quantum"
                )
                
                # Spin indicator
                if particle['spin'] > 0:
                    self.quantum_canvas.create_line(
                        particle['x'], particle['y'] - size - 2,
                        particle['x'], particle['y'] + size + 2,
                        fill=particle['color'], width=1, tags="quantum"
                    )
            
            # System title
            self.quantum_canvas.create_text(180, 25, text="QUANTUM OS v3.0", 
                                          font=('Arial', 14, 'bold'),
                                          fill='white', tags="quantum")
            self.quantum_canvas.create_text(180, 45, text="Neural Quantum Interface", 
                                          font=('Arial', 9),
                                          fill='#00ffff', tags="quantum")
            
            self.root.after(50, self.animate_quantum_field)

    def setup_neural_widgets(self):
        """Neural network powered widgets"""
        widgets_frame = tk.Frame(self.main_frame, bg='#0a0a0a', height=120)
        widgets_frame.pack(fill='x', pady=5)
        widgets_frame.pack_propagate(False)
        
        # Create neural widgets
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
        """Quantum application grid"""
        apps_frame = tk.Frame(self.main_frame, bg='#0a0a0a')
        apps_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create quantum app buttons
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
        """Get installed quantum apps"""
        self.q_cursor.execute('SELECT name, quantum_signature, neural_compatibility FROM quantum_apps')
        return self.q_cursor.fetchall()

    def setup_neural_navigation(self):
        """Neural navigation system"""
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

    def show_boot_screen(self):
        """Display a beautiful quantum boot screen"""
        self.boot_window = tk.Toplevel(self.root)
        self.boot_window.title("Quantum OS Booting...")
        self.boot_window.geometry(f"{self.screen_width}x{self.screen_height}")
        self.boot_window.configure(bg='#000000')
        self.boot_window.overrideredirect(True)  # Remove window decorations
        
        # Center the boot window
        self.boot_window.geometry(f"+{self.boot_window.winfo_screenwidth()//2 - self.screen_width//2}+{self.boot_window.winfo_screenheight()//2 - self.screen_height//2}")
        
        # Create boot canvas
        self.boot_canvas = tk.Canvas(self.boot_window, bg='#000000', 
                                   width=self.screen_width, height=self.screen_height,
                                   highlightthickness=0)
        self.boot_canvas.pack(fill='both', expand=True)
        
        # Boot animation particles
        self.boot_particles = []
        self.boot_waves = []
        self.boot_progress = 0
        self.boot_stage = 0
        
        self.initialize_boot_animation()
        self.animate_boot_sequence()

    def initialize_boot_animation(self):
        """Initialize boot animation elements"""
        # Create quantum particles for boot animation
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
        
        # Create wave patterns
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
        """Animate the boot sequence"""
        self.boot_canvas.delete("boot")
        
        center_x, center_y = self.screen_width // 2, self.screen_height // 2
        
        # Draw background waves
        for wave in self.boot_waves:
            points = []
            for x in range(0, self.screen_width + 10, 5):
                y = center_y + wave['amplitude'] * math.sin(wave['frequency'] * x + wave['phase'])
                points.extend([x, y])
            
            self.boot_canvas.create_line(points, fill=wave['color'], 
                                       width=2, tags="boot", smooth=True)
            wave['phase'] += wave['speed']
        
        # Draw quantum particles
        for particle in self.boot_particles:
            # Update position
            particle['x'] += particle['vx']
            particle['y'] += particle['vy']
            particle['pulse'] += 0.1
            
            # Boundary wrapping
            if particle['x'] < 0: particle['x'] = self.screen_width
            if particle['x'] > self.screen_width: particle['x'] = 0
            if particle['y'] < 0: particle['y'] = self.screen_height
            if particle['y'] > self.screen_height: particle['y'] = 0
            
            # Pulsing effect
            pulse_size = particle['size'] + math.sin(particle['pulse']) * 1.5
            
            self.boot_canvas.create_oval(
                particle['x'] - pulse_size, particle['y'] - pulse_size,
                particle['x'] + pulse_size, particle['y'] + pulse_size,
                fill=particle['color'], outline='', tags="boot"
            )
        
        # Draw quantum logo
        self.draw_quantum_logo(center_x, center_y)
        
        # Draw boot progress
        self.draw_boot_progress()
        
        # Update boot sequence
        self.update_boot_sequence()
        
        # Continue animation or finish
        if self.boot_stage < 100:
            self.boot_window.after(30, self.animate_boot_sequence)
        else:
            self.finish_boot_sequence()

    def draw_quantum_logo(self, center_x, center_y):
        """Draw the quantum OS logo"""
        # Main quantum sphere
        radius = 60
        self.boot_canvas.create_oval(
            center_x - radius, center_y - radius,
            center_x + radius, center_y + radius,
            outline='#00ffff', width=3, tags="boot"
        )
        
        # Rotating orbitals
        time_factor = time.time() * 2
        for i in range(3):
            angle = time_factor + i * 2 * math.pi / 3
            orbit_radius = radius + 15 + i * 10
            electron_x = center_x + orbit_radius * math.cos(angle)
            electron_y = center_y + orbit_radius * math.sin(angle)
            
            # Orbital path
            self.boot_canvas.create_oval(
                center_x - orbit_radius, center_y - orbit_radius,
                center_x + orbit_radius, center_y + orbit_radius,
                outline='#ff00ff', width=1, tags="boot", dash=(4, 4)
            )
            
            # Electron
            self.boot_canvas.create_oval(
                electron_x - 4, electron_y - 4,
                electron_x + 4, electron_y + 4,
                fill='#ffff00', outline='', tags="boot"
            )
        
        # Quantum core
        core_radius = 15
        pulse = math.sin(time.time() * 5) * 3 + core_radius
        self.boot_canvas.create_oval(
            center_x - pulse, center_y - pulse,
            center_x + pulse, center_y + pulse,
            fill='#00ffff', outline='', tags="boot"
        )
        
        # Logo text
        self.boot_canvas.create_text(
            center_x, center_y + radius + 40,
            text="QUANTUM OS", font=('Arial', 16, 'bold'),
            fill='#00ffff', tags="boot"
        )
        
        self.boot_canvas.create_text(
            center_x, center_y + radius + 60,
            text="v3.0 Neural Interface", font=('Arial', 10),
            fill='#cccccc', tags="boot"
        )

    def draw_boot_progress(self):
        """Draw boot progress bar and status messages"""
        # Progress bar background
        bar_width = 300
        bar_height = 12
        bar_x = (self.screen_width - bar_width) // 2
        bar_y = self.screen_height - 80
        
        self.boot_canvas.create_rectangle(
            bar_x, bar_y, bar_x + bar_width, bar_y + bar_height,
            outline='#333333', fill='#1a1a1a', width=2, tags="boot"
        )
        
        # Progress fill
        progress_width = (bar_width * self.boot_progress) // 100
        if progress_width > 0:
            self.boot_canvas.create_rectangle(
                bar_x, bar_y, bar_x + progress_width, bar_y + bar_height,
                fill='#00ffff', outline='', tags="boot"
            )
        
        # Progress percentage
        self.boot_canvas.create_text(
            self.screen_width // 2, bar_y - 20,
            text=f"{self.boot_progress}%", font=('Arial', 12, 'bold'),
            fill='#00ffff', tags="boot"
        )
        
        # Status messages based on boot stage
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
        """Update boot progress and stages"""
        if self.boot_stage < 100:
            # Increment progress with some randomness for natural feel
            increment = random.uniform(0.5, 2.0)
            self.boot_progress = min(100, self.boot_progress + increment)
            
            # Update stage based on progress
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
        """Finish boot sequence and show main interface"""
        # Fade out effect
        for alpha in range(100, -1, -5):
            self.boot_window.attributes('-alpha', alpha/100)
            self.boot_window.update()
            time.sleep(0.02)
        
        self.boot_window.destroy()
        self.root.deiconify()  # Show main window

    def launch_with_animation(self, signature):
        """Launch app with quantum transition animation"""
        if self.animation_running:
            return
            
        self.animation_running = True
        
        # Get app name
        self.q_cursor.execute('SELECT name FROM quantum_apps WHERE quantum_signature = ?', (signature,))
        result = self.q_cursor.fetchone()
        app_name = result[0] if result else "Quantum App"
        
        # Create overlay for animation
        self.animation_overlay = tk.Frame(self.root, bg='#0a0a0a')
        self.animation_overlay.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Create animation canvas
        self.anim_canvas = tk.Canvas(self.animation_overlay, bg='#0a0a0a', 
                                   highlightthickness=0)
        self.anim_canvas.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Start quantum transition animation
        self.quantum_transition_animation(app_name, signature, 0)

    def quantum_transition_animation(self, app_name, signature, frame):
        """Quantum-style transition animation"""
        self.anim_canvas.delete("transition")
        
        center_x, center_y = self.screen_width // 2, self.screen_height // 2
        
        # Pulsing quantum circles
        for i in range(3):
            radius = ((frame + i * 10) % 50) * 8
            alpha = max(0, 1 - radius / 400)
            color = f'#00{int(255 * alpha):02x}ff'
            
            self.anim_canvas.create_oval(
                center_x - radius, center_y - radius,
                center_x + radius, center_y + radius,
                outline=color, width=3, tags="transition"
            )
        
        # Rotating quantum shapes
        shapes = ['circle', 'triangle', 'square', 'hexagon']
        for i, shape in enumerate(shapes):
            angle = (frame * 5 + i * 90) * math.pi / 180
            distance = 50 + frame * 2
            x = center_x + distance * math.cos(angle)
            y = center_y + distance * math.sin(angle)
            
            if shape == 'circle':
                self.anim_canvas.create_oval(x-15, y-15, x+15, y+15, 
                                           outline='#ff00ff', width=2, tags="transition")
            elif shape == 'triangle':
                points = [x, y-15, x-15, y+15, x+15, y+15]
                self.anim_canvas.create_polygon(points, outline='#ffff00', width=2, 
                                              fill='', tags="transition")
            elif shape == 'square':
                self.anim_canvas.create_rectangle(x-15, y-15, x+15, y+15,
                                                outline='#00ff88', width=2, tags="transition")
            else:  # hexagon
                points = []
                for j in range(6):
                    angle_hex = j * 60 * math.pi / 180
                    points.extend([x + 15 * math.cos(angle_hex), 
                                 y + 15 * math.sin(angle_hex)])
                self.anim_canvas.create_polygon(points, outline='#ff4444', width=2, 
                                              fill='', tags="transition")
        
        # App name with fade-in effect
        alpha = min(1.0, frame / 30)
        text_color = f'#{"00"}{int(255 * alpha):02x}{"ff"}'
        self.anim_canvas.create_text(center_x, center_y, text=app_name,
                                   font=('Arial', 20, 'bold'), fill=text_color,
                                   tags="transition")
        
        if frame < 60:
            self.root.after(16, lambda: self.quantum_transition_animation(app_name, signature, frame + 1))
        else:
            # Animation complete
            self.animation_overlay.destroy()
            self.animation_running = False
            self.launch_quantum_app(signature)

    def launch_quantum_app(self, signature):
        """Launch the actual quantum application"""
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
            # اضافه کردن برنامه‌های جدید
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
            messagebox.showinfo("Quantum App", f"Launching {signature}")

    def update_quantum_status(self):
        """Update quantum system status"""
        current_time = datetime.now().strftime("%H:%M:%S")
        quantum_time = f"Q-TIME: {current_time}"
        self.quantum_time.config(text=quantum_time)
        
        # Update metrics with quantum fluctuations
        self.system_metrics['quantum_coherence'] = 98.5 + random.uniform(-0.2, 0.2)
        self.system_metrics['neural_throughput'] = 450 + random.randint(-10, 10)
        self.system_metrics['temporal_stability'] = 99.8 + random.uniform(-0.1, 0.1)
        
        self.coherence_label.config(text=f"QC: {self.system_metrics['quantum_coherence']:.1f}%")
        self.throughput_label.config(text=f"NT: {self.system_metrics['neural_throughput']}")
        self.stability_label.config(text=f"TS: {self.system_metrics['temporal_stability']:.1f}%")
        
        self.root.after(1000, self.update_quantum_status)

    def start_quantum_services(self):
        """Start quantum background services"""
        threading.Thread(target=self.quantum_processing, daemon=True).start()
        threading.Thread(target=self.neural_learning, daemon=True).start()
        threading.Thread(target=self.widget_quantum_updates, daemon=True).start()

    def quantum_processing(self):
        """Quantum background processing"""
        while True:
            # Simulate quantum computations
            time.sleep(2)
            # Update quantum state
            self.quantum_state = random.choice(["superposition", "entanglement", "coherence"])
            self.neural_activity = max(0.1, min(0.99, self.neural_activity + random.uniform(-0.05, 0.05)))

    def neural_learning(self):
        """Neural network learning process"""
        while True:
            # Simulate neural learning
            time.sleep(5)

    def widget_quantum_updates(self):
        """Update quantum widgets"""
        while True:
            for widget in self.neural_widgets:
                if hasattr(widget, 'quantum_update'):
                    try:
                        widget.quantum_update()
                    except:
                        pass
            time.sleep(3)

    def change_theme(self):
        """تغییر تم سیستم"""
        themes = list(self.themes.keys())
        themes.remove(self.current_theme)
        new_theme = random.choice(themes)
        
        theme = self.themes[new_theme]
        self.current_theme = new_theme
        
        # اعمال تم جدید
        self.root.configure(bg=theme['bg'])
        self.main_frame.configure(bg=theme['bg'])
        self.status_frame.configure(bg=theme['bg'])
        
        # به روز رسانی رنگ‌ها
        self.quantum_time.config(bg=theme['bg'], fg=theme['fg'])
        self.theme_btn.config(bg='#252525', fg=theme['accent'])
        
        messagebox.showinfo("Theme Changed", f"Theme changed to {new_theme.upper()}")

    def run(self):
        """Run quantum operating system with boot screen"""
        # Hide main window initially
        self.root.withdraw()
        
        # Show boot screen
        self.show_boot_screen()
        
        # Start main loop
        try:
            self.root.mainloop()
        finally:
            if hasattr(self, 'quantum_db'):
                self.quantum_db.close()

# برنامه‌های کاربردی اصلی (همان قبلی)
class QuantumPhone:
    """Fully functional phone app"""
    def __init__(self, os):
        self.os = os
        self.window = None
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Quantum Phone")
        self.window.geometry("500x600")
        self.window.configure(bg='#0a0a0a')
        
        # Header
        header = tk.Frame(self.window, bg='#1a1a1a', height=60)
        header.pack(fill='x')
        tk.Label(header, text="QUANTUM PHONE", font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='#00ffff').pack(expand=True)
        
        # Number display
        self.number_display = tk.Label(self.window, text="", font=('Arial', 20),
                                     bg='#1a1a1a', fg='white', width=15, height=2)
        self.number_display.pack(pady=10)
        
        # Keypad
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
        
        # Action buttons
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
        
        # Contacts button
        contacts_btn = tk.Button(action_frame, text="CONTACTS", font=('Arial', 12),
                               bg='#0088aa', fg='white', width=8,
                               command=self.show_contacts)
        contacts_btn.pack(side='left', padx=5)
        
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
            
    def show_contacts(self):
        """Show contacts list"""
        contacts_window = tk.Toplevel(self.window)
        contacts_window.title("Contacts")
        contacts_window.geometry("400x400")
        contacts_window.configure(bg='#0a0a0a')
        
        # Get contacts from database
        self.os.q_cursor.execute('SELECT name, number FROM contacts')
        contacts = self.os.q_cursor.fetchall()
        
        for name, number in contacts:
            contact_frame = tk.Frame(contacts_window, bg='#1a1a1a', height=50)
            contact_frame.pack(fill='x', padx=5, pady=2)
            
            name_label = tk.Label(contact_frame, text=name, font=('Arial', 12, 'bold'),
                                bg='#1a1a1a', fg='white', anchor='w')
            name_label.pack(anchor='w', padx=10, pady=2)
            
            number_label = tk.Label(contact_frame, text=number, font=('Arial', 10),
                                  bg='#1a1a1a', fg='#cccccc', anchor='w')
            number_label.pack(anchor='w', padx=10)
            
            # Call button for each contact
            call_btn = tk.Button(contact_frame, text="CALL", font=('Arial', 8),
                               bg='#00aa00', fg='white',
                               command=lambda n=number: self.call_contact(n))
            call_btn.place(relx=0.8, rely=0.3)
    
    def call_contact(self, number):
        self.number_display.config(text=number)
        self.make_call()

class NeuralMessenger:
    """Fully functional messaging app"""
    def __init__(self, os):
        self.os = os
        self.window = None
        self.current_chat = None
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Neural Messenger")
        self.window.geometry("400x500")
        self.window.configure(bg='#0a0a0a')
        
        # Header
        header = tk.Frame(self.window, bg='#1a1a1a', height=60)
        header.pack(fill='x')
        tk.Label(header, text="NEURAL MESSENGER", font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='#00ffff').pack(expand=True)
        
        # Contacts list
        contacts_frame = tk.Frame(self.window, bg='#0a0a0a')
        contacts_frame.pack(fill='both', expand=True)
        
        # Get contacts from database
        self.os.q_cursor.execute('SELECT name FROM contacts')
        contacts = self.os.q_cursor.fetchall()
        
        for (name,) in contacts:
            contact_btn = tk.Button(contacts_frame, text=name, font=('Arial', 12),
                                  bg='#1a1a1a', fg='white', height=2,
                                  command=lambda n=name: self.open_chat(n))
            contact_btn.pack(fill='x', padx=10, pady=2)
    
    def open_chat(self, contact):
        """Open chat with contact"""
        chat_window = tk.Toplevel(self.window)
        chat_window.title(f"Chat with {contact}")
        chat_window.geometry("300x400")
        chat_window.configure(bg='#0a0a0a')
        
        # Header
        header = tk.Frame(chat_window, bg='#1a1a1a', height=50)
        header.pack(fill='x')
        tk.Label(header, text=contact, font=('Arial', 14, 'bold'),
                bg='#1a1a1a', fg='white').pack(expand=True)
        
        # Chat display
        chat_display = scrolledtext.ScrolledText(chat_window, 
                                               bg='#0a0a0a', fg='white',
                                               font=('Arial', 10), wrap=tk.WORD)
        chat_display.pack(fill='both', expand=True, padx=10, pady=10)
        chat_display.config(state=tk.DISABLED)
        
        # Load existing messages
        self.os.q_cursor.execute('SELECT message, timestamp, is_sent FROM messages WHERE contact = ?', (contact,))
        messages = self.os.q_cursor.fetchall()
        
        # Display messages
        chat_display.config(state=tk.NORMAL)
        for message, timestamp, is_sent in messages:
            sender = "You" if is_sent else contact
            chat_display.insert(tk.END, f"[{timestamp}] {sender}: {message}\n\n")
        chat_display.config(state=tk.DISABLED)
        chat_display.see(tk.END)
        
        # Message input
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
                
                # Save message to database
                self.os.q_cursor.execute('''
                    INSERT INTO messages (contact, message, timestamp, is_sent)
                    VALUES (?, ?, ?, ?)
                ''', (contact, message, current_time, True))
                self.os.quantum_db.commit()
                
                # Auto-reply
                chat_display.config(state=tk.NORMAL)
                replies = [
                    "Interesting! Tell me more.",
                    "Quantum computing is the future!",
                    "I need to learn more about that.",
                    "That's amazing progress!",
                    "Fascinating quantum insights!"
                ]
                reply = random.choice(replies)
                chat_display.insert(tk.END, f"[{current_time}] {contact}: {reply}\n\n")
                chat_display.config(state=tk.DISABLED)
                chat_display.see(tk.END)
        
        message_entry.bind('<Return>', lambda e: send_message())
        
        send_btn = tk.Button(input_frame, text="SEND", font=('Arial', 9),
                           bg='#00aa00', fg='white', command=send_message)
        send_btn.pack(side='right', padx=(5, 0))

class AICamera:
    """AI-powered camera app without OpenCV"""
    def __init__(self, os):
        self.os = os
        self.window = None
        self.camera_active = False
        self.animation_id = None
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("AI Camera")
        self.window.geometry("400x600")
        self.window.configure(bg='black')
        
        # Header
        header = tk.Frame(self.window, bg='#1a1a1a', height=50)
        header.pack(fill='x')
        tk.Label(header, text="AI CAMERA", font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='#00ffff').pack(expand=True)
        
        # Viewfinder
        self.viewfinder = tk.Label(self.window, text="QUANTUM CAMERA READY\nNeural Processing Active", 
                                 font=('Arial', 12), bg='#333333', fg='white',
                                 width=40, height=15)
        self.viewfinder.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Controls
        controls = tk.Frame(self.window, bg='#1a1a1a', height=80)
        controls.pack(fill='x')
        
        # Start/Stop camera button
        self.camera_btn = tk.Button(controls, text="START CAMERA", font=('Arial', 12),
                                  bg='#00aa00', fg='white', width=12,
                                  command=self.toggle_camera)
        self.camera_btn.pack(side='left', padx=10, pady=10)
        
        # Capture button
        capture_btn = tk.Button(controls, text="CAPTURE", font=('Arial', 12),
                              bg='#ff4444', fg='white', width=8,
                              command=self.capture_photo)
        capture_btn.pack(side='right', padx=10, pady=10)
        
        # Mode selector
        mode_frame = tk.Frame(self.window, bg='#1a1a1a')
        mode_frame.pack(fill='x')
        
        modes = ["PHOTO", "VIDEO", "PORTRAIT", "NIGHT"]
        for mode in modes:
            mode_btn = tk.Button(mode_frame, text=mode, font=('Arial', 8),
                               bg='#2a2a2a', fg='white', width=8,
                               command=lambda m=mode: self.set_mode(m))
            mode_btn.pack(side='left', expand=True, padx=2, pady=5)
        
        # Status
        self.status_label = tk.Label(self.window, text="Camera: READY - Quantum Enhanced", 
                                   font=('Arial', 9), bg='black', fg='#00ff88')
        self.status_label.pack(side='bottom', fill='x')
        
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def toggle_camera(self):
        if not self.camera_active:
            self.start_camera()
        else:
            self.stop_camera()
    
    def start_camera(self):
        self.camera_active = True
        self.camera_btn.config(text="STOP CAMERA", bg='#aa0000')
        self.status_label.config(text="Camera: ACTIVE - AI Processing Enabled")
        self.simulate_camera_feed()
    
    def stop_camera(self):
        self.camera_active = False
        self.camera_btn.config(text="START CAMERA", bg='#00aa00')
        self.status_label.config(text="Camera: READY - Quantum Enhanced")
        
        if self.animation_id:
            self.window.after_cancel(self.animation_id)
            self.animation_id = None
        
        self.viewfinder.config(text="QUANTUM CAMERA READY\nNeural Processing Active", 
                             bg='#333333', fg='white', image='')
    
    def simulate_camera_feed(self):
        """Create animated camera simulation"""
        if not self.camera_active:
            return
            
        # Create a simulated camera image using PIL
        width, height = 300, 400
        img = Image.new('RGB', (width, height), color='#1a1a1a')
        draw = ImageDraw.Draw(img)
        
        # Add camera frame
        draw.rectangle([10, 10, width-10, height-10], outline='#00ffff', width=3)
        
        # Add moving quantum particles
        current_time = time.time()
        for i in range(20):
            x = int((math.sin(current_time + i) + 1) * (width - 40) / 2) + 20
            y = int((math.cos(current_time * 0.7 + i) + 1) * (height - 40) / 2) + 20
            size = random.randint(2, 6)
            color = random.choice(['#00ffff', '#ff00ff', '#ffff00', '#00ff88'])
            draw.ellipse([x-size, y-size, x+size, y+size], fill=color)
        
        # Add AI processing info
        draw.text((20, 20), "QUANTUM CAMERA ACTIVE", fill='#00ffff')
        draw.text((20, 40), "AI Processing: ENABLED", fill='#00ff88')
        draw.text((20, 60), f"Neural Net: {int((current_time * 10) % 100)}%", fill='#ff44ff')
        draw.text((20, 80), "Quantum Filter: ACTIVE", fill='#ffff00')
        
        # Add focus points
        for i in range(5):
            angle = current_time * 2 + i * 1.2
            radius = 80 + math.sin(angle) * 20
            x = width // 2 + int(math.cos(angle) * radius)
            y = height // 2 + int(math.sin(angle) * radius)
            draw.rectangle([x-2, y-2, x+2, y+2], fill='#ff4444')
        
        # Convert to PhotoImage
        img_tk = ImageTk.PhotoImage(img)
        
        self.viewfinder.config(image=img_tk, text="")
        self.viewfinder.image = img_tk
        
        # Continue animation
        if self.camera_active:
            self.animation_id = self.window.after(50, self.simulate_camera_feed)
    
    def capture_photo(self):
        if self.camera_active:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"quantum_photo_{timestamp}.png"
            
            # Create a final image for the photo
            width, height = 300, 400
            img = Image.new('RGB', (width, height), color='#1a1a1a')
            draw = ImageDraw.Draw(img)
            
            # Add photo frame
            draw.rectangle([5, 5, width-5, height-5], outline='#00ffff', width=2)
            
            # Add captured content
            current_time = time.time()
            for i in range(50):  # More particles for final photo
                x = random.randint(10, width-10)
                y = random.randint(10, height-10)
                size = random.randint(1, 4)
                color = random.choice(['#00ffff', '#ff00ff', '#ffff00', '#00ff88', '#ff4444'])
                draw.ellipse([x-size, y-size, x+size, y+size], fill=color)
            
            # Add capture info
            draw.text((width//2, 20), "QUANTUM PHOTO", fill='#00ffff', anchor='mt')
            draw.text((width//2, 40), f"Captured: {timestamp}", fill='#cccccc', anchor='mt')
            draw.text((width//2, 60), "AI Enhanced", fill='#00ff88', anchor='mt')
            draw.text((width//2, 80), "Neural Processed", fill='#ff44ff', anchor='mt')
            
            # Save the image
            try:
                img.save(filename)
                messagebox.showinfo("Photo Captured", 
                                  f"Quantum photo saved as: {filename}\n\n"
                                  f"AI Enhancement: Applied\n"
                                  f"Neural Filters: Active\n"
                                  f"Quantum Processing: Complete")
            except Exception as e:
                messagebox.showinfo("Photo Captured", 
                                  f"Photo simulated successfully!\n\n"
                                  f"AI Enhancement: Applied\n"
                                  f"Neural Filters: Active\n"
                                  f"Quantum Processing: Complete")
        else:
            messagebox.showwarning("Camera Not Active", "Please start the camera first")
    
    def set_mode(self, mode):
        self.status_label.config(text=f"Mode: {mode} - AI adjustments applied")
    
    def on_close(self):
        self.stop_camera()
        self.window.destroy()

class QuantumBrowser:
    """Fully functional web browser"""
    def __init__(self, os):
        self.os = os
        self.window = None
        self.history = []
        self.current_page = 0
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Quantum Browser")
        self.window.geometry("500x600")
        self.window.configure(bg='#0a0a0a')
        
        # Address bar
        address_frame = tk.Frame(self.window, bg='#2a2a2a', height=40)
        address_frame.pack(fill='x')
        
        self.address_bar = tk.Entry(address_frame, font=('Arial', 10),
                                  bg='#1a1a1a', fg='white', relief='flat')
        self.address_bar.pack(fill='x', padx=5, pady=5)
        self.address_bar.insert(0, "https://quantum-browser.com")
        self.address_bar.bind('<Return>', self.navigate)
        
        # Navigation buttons
        nav_frame = tk.Frame(self.window, bg='#1a1a1a', height=35)
        nav_frame.pack(fill='x')
        
        back_btn = tk.Button(nav_frame, text="←", font=('Arial', 12),
                           bg='#2a2a2a', fg='white', width=3,
                           command=self.go_back)
        back_btn.pack(side='left', padx=2)
        
        forward_btn = tk.Button(nav_frame, text="→", font=('Arial', 12),
                              bg='#2a2a2a', fg='white', width=3,
                              command=self.go_forward)
        forward_btn.pack(side='left', padx=2)
        
        refresh_btn = tk.Button(nav_frame, text="↻", font=('Arial', 12),
                              bg='#2a2a2a', fg='white', width=3,
                              command=self.refresh)
        refresh_btn.pack(side='left', padx=2)
        
        home_btn = tk.Button(nav_frame, text="⌂", font=('Arial', 12),
                           bg='#2a2a2a', fg='white', width=3,
                           command=self.go_home)
        home_btn.pack(side='left', padx=2)
        
        # Content display
        self.content_frame = tk.Frame(self.window, bg='white')
        self.content_frame.pack(fill='both', expand=True)
        
        self.show_home_page()
    
    def show_home_page(self):
        """Show browser home page"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()
            
        content = """
        QUANTUM BROWSER
        
        Welcome to Quantum Web Experience!
        
        Features:
        • Quantum Encryption
        • Neural Search
        • AI-Powered Browsing
        • Secure Connections
        
        Try searching for:
        - Quantum Computing
        - Neural Networks
        - AI Research
        - Quantum Physics
        """
        
        content_label = tk.Label(self.content_frame, text=content, 
                               font=('Arial', 11), justify='center', bg='white')
        content_label.pack(expand=True, pady=20)
        
        self.history.append("home")
        self.current_page = len(self.history) - 1
    
    def navigate(self, event=None):
        url = self.address_bar.get().lower()
        self.history.append(url)
        self.current_page = len(self.history) - 1
        
        if 'quantum' in url:
            content = """
            QUANTUM COMPUTING
            
            Quantum computing uses quantum mechanics
            to process information in new ways.
            
            Key Concepts:
            • Qubits
            • Superposition
            • Entanglement
            • Quantum Gates
            
            Current Applications:
            - Cryptography
            - Drug Discovery
            - Optimization
            - AI Acceleration
            """
        elif 'neural' in url or 'ai' in url:
            content = """
            ARTIFICIAL INTELLIGENCE
            
            AI systems are transforming technology
            and society.
            
            Neural Networks:
            • Deep Learning
            • Machine Learning
            • Computer Vision
            • Natural Language
            
            Quantum AI:
            - Faster Training
            - Better Optimization
            - Enhanced Security
            """
        else:
            content = """
            PAGE NOT FOUND
            
            The quantum page you're looking for
            doesn't exist in this reality.
            
            Try searching for:
            - Quantum
            - Neural
            - AI
            - Computing
            """
        
        for widget in self.content_frame.winfo_children():
            widget.destroy()
            
        content_label = tk.Label(self.content_frame, text=content, 
                               font=('Arial', 10), justify='center', bg='white')
        content_label.pack(expand=True, pady=20)
    
    def go_back(self):
        if self.current_page > 0:
            self.current_page -= 1
            self.navigate_to_history()
    
    def go_forward(self):
        if self.current_page < len(self.history) - 1:
            self.current_page += 1
            self.navigate_to_history()
    
    def navigate_to_history(self):
        if self.history:
            page = self.history[self.current_page]
            if page == "home":
                self.show_home_page()
            else:
                self.address_bar.delete(0, tk.END)
                self.address_bar.insert(0, page)
                self.navigate()
    
    def refresh(self):
        self.navigate()
    
    def go_home(self):
        self.address_bar.delete(0, tk.END)
        self.address_bar.insert(0, "https://quantum-browser.com")
        self.show_home_page()

class QuantumCalculator:
    """Fully functional calculator"""
    def __init__(self, os):
        self.os = os
        self.window = None
        self.current_input = "0"
        self.operator = None
        self.previous_input = None
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Quantum Calculator")
        self.window.geometry("700x500")
        self.window.configure(bg='#0a0a0a')
        
        # Display
        self.display = tk.Label(self.window, text=self.current_input, font=('Arial', 20),
                              bg='#1a1a1a', fg='white', width=15, height=2, anchor='e')
        self.display.pack(pady=10)
        
        # Buttons
        buttons = [
            'C', '±', '%', '÷',
            '7', '8', '9', '×',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', 'Del', '.', '='
        ]
        
        button_frame = tk.Frame(self.window, bg='#0a0a0a')
        button_frame.pack(expand=True, fill='both', padx=10, pady=10)
        
        for i, text in enumerate(buttons):
            if text:
                row = i // 4
                col = i % 4
                
                if text == '=':
                    bg_color = '#0088ff'
                elif text in ['C', '±', '%']:
                    bg_color = '#666666'
                elif text in ['÷', '×', '-', '+']:
                    bg_color = '#ff8800'
                else:
                    bg_color = '#444444'
                
                btn = tk.Button(button_frame, text=text, font=('Arial', 14),
                              bg=bg_color, fg='white', width=4, height=2,
                              command=lambda t=text: self.button_click(t))
                btn.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')
                
                button_frame.grid_columnconfigure(col, weight=1)
                button_frame.grid_rowconfigure(row, weight=1)

    def button_click(self, text):
        if text.isdigit() or text == '.':
            self.input_number(text)
        elif text in ['+', '-', '×', '÷']:
            self.input_operator(text)
        elif text == '=':
            self.calculate()
        elif text == 'C':
            self.clear()
        elif text == 'Del':
            self.clear()
        elif text == '±':
            self.toggle_sign()
        elif text == '%':
            self.percentage()

    def input_number(self, num):
        if self.current_input == "0" or self.operator == "=":
            self.current_input = num
        else:
            self.current_input += num
        self.update_display()

    def input_operator(self, op):
        if self.previous_input is None:
            self.previous_input = self.current_input
        else:
            self.calculate()
        self.operator = op
        self.current_input = "0"

    def calculate(self):
        if self.previous_input is not None and self.operator is not None:
            try:
                prev = float(self.previous_input)
                curr = float(self.current_input)
                
                if self.operator == '+':
                    result = prev + curr
                elif self.operator == '-':
                    result = prev - curr
                elif self.operator == '×':
                    result = prev * curr
                elif self.operator == '÷':
                    if curr != 0:
                        result = prev / curr
                    else:
                        result = "Error"
                else:
                    result = curr
                
                # Add quantum fluctuation for fun
                if isinstance(result, float) and random.random() < 0.1:
                    fluctuation = random.uniform(-0.0001, 0.0001)
                    result += result * fluctuation
                
                self.current_input = str(result)
                self.operator = "="
                self.previous_input = None
                self.update_display()
                
            except:
                self.current_input = "Error"
                self.update_display()

    def clear(self):
        self.current_input = "0"
        self.previous_input = None
        self.operator = None
        self.update_display()

    def toggle_sign(self):
        if self.current_input != "0":
            if self.current_input.startswith('-'):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = '-' + self.current_input
        self.update_display()

    def percentage(self):
        try:
            value = float(self.current_input) / 100
            self.current_input = str(value)
            self.update_display()
        except:
            self.current_input = "Error"
            self.update_display()

    def update_display(self):
        display_text = self.current_input
        if len(display_text) > 12:
            display_text = display_text[:12]
        self.display.config(text=display_text)

class TemporalCalendar:
    """Calendar app with quantum features"""
    def __init__(self, os):
        self.os = os
        self.window = None
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Temporal Calendar")
        self.window.geometry("600x600")
        self.window.configure(bg='#0a0a0a')
        
        # Header
        header = tk.Frame(self.window, bg='#1a1a1a', height=50)
        header.pack(fill='x')
        
        today = datetime.now()
        month_year = today.strftime("%B %Y")
        tk.Label(header, text=month_year, font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='white').pack(expand=True)
        
        # Days of week
        days_frame = tk.Frame(self.window, bg='#0a0a0a')
        days_frame.pack(fill='x')
        
        days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
        for day in days:
            tk.Label(days_frame, text=day, font=('Arial', 10),
                   bg='#0a0a0a', fg='#888888', width=5).pack(side='left')
        
        # Calendar grid
        calendar_frame = tk.Frame(self.window, bg='#0a0a0a')
        calendar_frame.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Simple calendar display
        today_day = today.day
        for i in range(1, 32):
            day_btn = tk.Button(calendar_frame, text=str(i), font=('Arial', 10),
                              bg='#1a1a1a' if i != today_day else '#00aa00',
                              fg='white' if i != today_day else 'black',
                              width=4, height=2,
                              command=lambda d=i: self.select_day(d))
            row = (i - 1) // 7
            col = (i - 1) % 7
            day_btn.grid(row=row, column=col, padx=2, pady=2)
        
        # Events section
        events_frame = tk.Frame(self.window, bg='#1a1a1a', height=80)
        events_frame.pack(fill='x', side='bottom')
        events_frame.pack_propagate(False)
        
        tk.Label(events_frame, text="Today's Events:", font=('Arial', 10, 'bold'),
                bg='#1a1a1a', fg='white').pack(anchor='w', padx=10, pady=5)
        
        events = [
            "10:00 - Quantum Meeting",
            "14:00 - Neural Network Training", 
            "16:00 - AI Research Discussion"
        ]
        
        for event in events:
            tk.Label(events_frame, text=event, font=('Arial', 8),
                   bg='#1a1a1a', fg='#cccccc', anchor='w').pack(anchor='w', padx=20)
    
    def select_day(self, day):
        messagebox.showinfo("Calendar", f"Selected: {datetime.now().strftime('%B')} {day}\n\nQuantum scheduling activated")

class QuantumAIAssistant:
    """Quantum AI Assistant"""
    def __init__(self, os):
        self.os = os
        self.window = None
        self.ai_processor = QuantumAIProcessor()
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Quantum AI Assistant")
        self.window.geometry("500x700")
        self.window.configure(bg='#0f0f0f')
        
        # Quantum AI Header
        header = tk.Frame(self.window, bg='#1a1a1a', height=70)
        header.pack(fill='x')
        
        tk.Label(header, text="QUANTUM AI ASSISTANT", 
                font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='#00ffff').pack(expand=True, pady=10)
        
        tk.Label(header, text="Neural Quantum Network v4.2", 
                font=('Arial', 9),
                bg='#1a1a1a', fg='#888888').pack()
        
        # Quantum Chat Display
        self.chat_display = scrolledtext.ScrolledText(self.window, 
                                                    bg='#0f0f0f', fg='#00ff88',
                                                    font=('Arial', 10), wrap=tk.WORD)
        self.chat_display.pack(fill='both', expand=True, padx=15, pady=15)
        self.chat_display.config(state=tk.DISABLED)
        
        # Quantum Input
        input_frame = tk.Frame(self.window, bg='#0f0f0f')
        input_frame.pack(fill='x', padx=15, pady=10)
        
        self.ai_input = tk.Entry(input_frame, font=('Arial', 11),
                               bg='#252525', fg='white')
        self.ai_input.pack(side='left', fill='x', expand=True, ipady=6)
        self.ai_input.bind('<Return>', self.process_quantum_query)
        
        quantum_btn = tk.Button(input_frame, text="QUANTUM", 
                              command=self.process_quantum_query,
                              bg='#00ffff', fg='black',
                              font=('Arial', 9, 'bold'))
        quantum_btn.pack(side='right', padx=(10, 0), ipadx=8)
        
        # Initial quantum message
        self.add_quantum_message("Quantum AI", "Neural quantum network initialized. Ready for quantum processing queries.\n\nTry: 'quantum', 'system', 'time', 'compute', or 'help'")

    def process_quantum_query(self, event=None):
        query = self.ai_input.get().strip()
        if query:
            self.add_quantum_message("User", query)
            response = self.ai_processor.process_quantum_query(query)
            self.add_quantum_message("Quantum AI", response)
            self.ai_input.delete(0, tk.END)
            
    def add_quantum_message(self, sender, message):
        self.chat_display.config(state=tk.NORMAL)
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.chat_display.insert(tk.END, f"[{timestamp}] {sender}: {message}\n\n")
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)

class NeuralFileSystem:
    """سیستم مدیریت فایل پیشرفته با دسترسی کامل"""
    def __init__(self, os):
        self.os = os
        self.window = None
        self.current_path = os.path.expanduser("~")
        self.file_list = []
        self.selected_file = None
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Neural File System - Quantum Access")
        self.window.geometry("600x700")
        self.window.configure(bg='#0a0a0a')
        
        # Header
        header = tk.Frame(self.window, bg='#1a1a1a', height=60)
        header.pack(fill='x', padx=10, pady=5)
        
        tk.Label(header, text="NEURAL FILE SYSTEM", font=('Arial', 18, 'bold'),
                bg='#1a1a1a', fg='#00ffff').pack(side='left', padx=10)
        
        # Current path display
        self.path_label = tk.Label(header, text=self.current_path, font=('Arial', 10),
                                 bg='#1a1a1a', fg='#cccccc', wraplength=400)
        self.path_label.pack(side='right', padx=10)
        
        # Navigation buttons
        nav_frame = tk.Frame(self.window, bg='#0a0a0a')
        nav_frame.pack(fill='x', padx=10, pady=5)
        
        home_btn = tk.Button(nav_frame, text="Home", font=('Arial', 10),
                           bg='#252525', fg='white', command=self.go_home)
        home_btn.pack(side='left', padx=5)
        
        back_btn = tk.Button(nav_frame, text="Back", font=('Arial', 10),
                           bg='#252525', fg='white', command=self.go_back)
        back_btn.pack(side='left', padx=5)
        
        refresh_btn = tk.Button(nav_frame, text="Refresh", font=('Arial', 10),
                              bg='#252525', fg='white', command=self.refresh_files)
        refresh_btn.pack(side='left', padx=5)
        
        # Search box
        search_frame = tk.Frame(self.window, bg='#0a0a0a')
        search_frame.pack(fill='x', padx=10, pady=5)
        
        tk.Label(search_frame, text="Search:", font=('Arial', 10),
                bg='#0a0a0a', fg='white').pack(side='left')
        
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, textvariable=self.search_var,
                              font=('Arial', 10), bg='#2a2a2a', fg='white')
        search_entry.pack(side='left', fill='x', expand=True, padx=5)
        search_entry.bind('<KeyRelease>', self.search_files)
        
        # File list with scrollbar
        list_frame = tk.Frame(self.window, bg='#0a0a0a')
        list_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Treeview for files
        columns = ('name', 'size', 'type', 'modified')
        self.tree = ttk.Treeview(list_frame, columns=columns, show='headings', height=20)
        
        # Define headings
        self.tree.heading('name', text='Name')
        self.tree.heading('size', text='Size')
        self.tree.heading('type', text='Type')
        self.tree.heading('modified', text='Modified')
        
        # Configure columns
        self.tree.column('Name', width=300)
        self.tree.column('Size', width=100)
        self.tree.column('Type', width=150)
        self.tree.column('Modified', width=150)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        
        self.tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Bind double click
        self.tree.bind("<Double-1>", self.on_double_click)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        
        # Action buttons
        action_frame = tk.Frame(self.window, bg='#0a0a0a')
        action_frame.pack(fill='x', padx=10, pady=10)
        
        open_btn = tk.Button(action_frame, text="Open", font=('Arial', 10),
                           bg='#0088ff', fg='white', width=10, command=self.open_file)
        open_btn.pack(side='left', padx=5)
        
        delete_btn = tk.Button(action_frame, text="Delete", font=('Arial', 10),
                             bg='#ff4444', fg='white', width=10, command=self.delete_file)
        delete_btn.pack(side='left', padx=5)
        
        new_folder_btn = tk.Button(action_frame, text="New Folder", font=('Arial', 10),
                                 bg='#00aa00', fg='white', width=12, command=self.create_folder)
        new_folder_btn.pack(side='left', padx=5)
        
        upload_btn = tk.Button(action_frame, text="Upload", font=('Arial', 10),
                             bg='#ff8800', fg='white', width=10, command=self.upload_file)
        upload_btn.pack(side='left', padx=5)
        
        properties_btn = tk.Button(action_frame, text="Properties", font=('Arial', 10),
                                 bg='#8844ff', fg='white', width=12, command=self.show_properties)
        properties_btn.pack(side='left', padx=5)
        
        # Status bar
        self.status_label = tk.Label(self.window, text="Ready", font=('Arial', 9),
                                   bg='#1a1a1a', fg='#00ff88', anchor='w')
        self.status_label.pack(fill='x', padx=10, pady=5)
        
        # Load initial files
        self.refresh_files()
        
        # Set style for treeview
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("Treeview", background="#1a1a1a", foreground="white", fieldbackground="#1a1a1a")
        style.configure("Treeview.Heading", background="#252525", foreground="#00ffff")
        style.map('Treeview', background=[('selected', '#005588')])

    def refresh_files(self):
        """بارگذاری فایل‌ها و پوشه‌ها"""
        self.tree.delete(*self.tree.get_children())
        self.file_list = []
        
        try:
            # پوشه والد
            if self.current_path != os.path.dirname(self.current_path):
                self.tree.insert('', 'end', text="..", values=("..", "", "Parent Directory", ""))
            
            # لیست محتویات
            for item in os.listdir(self.current_path):
                item_path = os.path.join(self.current_path, item)
                try:
                    if os.path.isdir(item_path):
                        size = ""
                        file_type = "Folder"
                    else:
                        size = self.format_size(os.path.getsize(item_path))
                        file_type = self.get_file_type(item)
                    
                    modified = datetime.fromtimestamp(os.path.getmtime(item_path)).strftime('%Y-%m-%d %H:%M')
                    self.tree.insert('', 'end', text=item, values=(item, size, file_type, modified))
                    
                    self.file_list.append(item_path)
                    
                except (OSError, PermissionError):
                    continue
                    
        except PermissionError:
            messagebox.showerror("Error", "Permission denied to access this directory")
            
    def format_size(self, size_bytes):
        """فرمت کردن سایز فایل"""
        if size_bytes == 0:
            return "0 B"
        size_names = ["B", "KB", "MB", "GB", "TB"]
        i = 0
        while size_bytes >= 1024 and i < len(size_names)-1:
            size_bytes /= 1024.0
            i += 1
        return f"{size_bytes:.1f} {size_names[i]}"
    
    def get_file_type(self, filename):
        """تعیین نوع فایل"""
        ext = os.path.splitext(filename)[1].lower()
        file_types = {
            '.txt': 'Text File', '.pdf': 'PDF Document', '.doc': 'Word Document',
            '.docx': 'Word Document', '.xls': 'Excel File', '.xlsx': 'Excel File',
            '.jpg': 'JPEG Image', '.png': 'PNG Image', '.mp3': 'Audio File',
            '.mp4': 'Video File', '.zip': 'Archive', '.exe': 'Application'
        }
        return file_types.get(ext, 'File')
    
    def create_folder(self):
        """ایجاد پوشه جدید"""
        name = simpledialog.askstring("New Folder", "Enter folder name:")
        if name:
            try:
                os.makedirs(os.path.join(self.current_path, name))
                self.refresh_files()
            except Exception as e:
                messagebox.showerror("Error", f"Cannot create folder: {str(e)}")
    
    def create_file(self):
        """ایجاد فایل جدید"""
        name = simpledialog.askstring("New File", "Enter file name:")
        if name:
            try:
                with open(os.path.join(self.current_path, name), 'w') as f:
                    f.write("")
                self.refresh_files()
            except Exception as e:
                messagebox.showerror("Error", f"Cannot create file: {str(e)}")
    
    def upload_file(self):
        """آپلود فایل"""
        file_path = filedialog.askopenfilename(title="Select file to upload")
        if file_path:
            try:
                shutil.copy2(file_path, self.current_path)
                self.refresh_files()
            except Exception as e:
                messagebox.showerror("Error", f"Cannot upload file: {str(e)}")
    
    def search_files(self, event=None):
        """جستجوی فایل‌ها"""
        query = self.search_var.get().lower()
        
        if not query:
            self.refresh_files()
            return
        
        # Filter files based on search query
        for item in self.tree.get_children():
            values = self.tree.item(item, 'values')
            filename = values[0].lower()
            if query in filename:
                self.tree.item(item, tags=('highlight',))
            else:
                self.tree.detach(item)
        
        self.tree.tag_configure('highlight', background='#005500')
    
    def show_properties(self):
        """نمایش خصوصیات آیتم"""
        selection = self.tree.selection()
        if selection:
            item = selection[0]
            name = self.tree.item(item, 'text')
            item_path = os.path.join(self.current_path, name)
            
            try:
                stats = os.stat(item_path)
                is_dir = os.path.isdir(item_path)
                
                properties = f"""
Name: {name}
Path: {item_path}
Type: {'Directory' if is_dir else 'File'}
Size: {self.format_size(stats.st_size) if not is_dir else 'N/A'}
Created: {datetime.fromtimestamp(stats.st_ctime)}
Modified: {datetime.fromtimestamp(stats.st_mtime)}
Accessed: {datetime.fromtimestamp(stats.st_atime)}
                """
                messagebox.showinfo("Properties", properties)
                
            except Exception as e:
                messagebox.showerror("Error", f"Cannot get properties: {str(e)}")

    def on_double_click(self, event):
        """Handle double click on files/folders"""
        item = self.tree.selection()[0]
        values = self.tree.item(item, 'values')
        name = values[0]
        
        if name == '..':
            self.go_back()
        elif values[2] == 'Folder':
            # It's a directory
            new_path = os.path.join(self.current_path, name)
            self.current_path = new_path
            self.refresh_files()
        else:
            # It's a file - open it
            self.open_file()

    def on_select(self, event):
        """Handle file selection"""
        selection = self.tree.selection()
        if selection:
            item = selection[0]
            values = self.tree.item(item, 'values')
            self.selected_file = values[0]
            self.status_label.config(text=f"Selected: {self.selected_file}")

    def go_home(self):
        """Go to home directory"""
        self.current_path = os.path.expanduser("~")
        self.refresh_files()

    def go_back(self):
        """Go to parent directory"""
        parent_dir = os.path.dirname(self.current_path)
        if parent_dir != self.current_path:
            self.current_path = parent_dir
            self.refresh_files()

    def open_file(self):
        """Open selected file"""
        if not self.selected_file:
            messagebox.showwarning("No Selection", "Please select a file first")
            return
        
        file_path = os.path.join(self.current_path, self.selected_file)
        
        try:
            if os.path.isdir(file_path):
                self.current_path = file_path
                self.refresh_files()
            else:
                # Try to open file with default application
                if os.name == 'nt':  # Windows
                    os.startfile(file_path)
                elif os.name == 'posix':  # macOS, Linux
                    os.system(f'xdg-open "{file_path}"')
                
                self.status_label.config(text=f"Opened: {self.selected_file}")
                
        except Exception as e:
            messagebox.showerror("Error", f"Cannot open file: {str(e)}")

    def delete_file(self):
        """حذف آیتم انتخاب شده"""
        selection = self.tree.selection()
        if selection:
            item = selection[0]
            name = self.tree.item(item, 'text')
            
            if messagebox.askyesno("Confirm Delete", f"Delete '{name}'?"):
                try:
                    item_path = os.path.join(self.current_path, name)
                    if os.path.isdir(item_path):
                        shutil.rmtree(item_path)
                    else:
                        os.remove(item_path)
                    self.refresh_files()
                except Exception as e:
                    messagebox.showerror("Error", f"Cannot delete: {str(e)}")

# برنامه‌های جدید که درخواست کردید:

class QuantumMusic:
    """پخش کننده موسیقی کوانتومی"""
    def __init__(self, os):
        self.os = os
        self.window = None
        self.current_track = 0
        self.playing = False
        self.tracks = [
            "Quantum Symphony - Neural Beats",
            "Temporal Waves - AI Generated", 
            "Photon Dance - Electronic Quantum",
            "Neural Network - Deep Learning",
            "Quantum Entanglement - Cosmic Sounds"
        ]
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Quantum Music Player")
        self.window.geometry("400x500")
        self.window.configure(bg='#0a0a0a')
        
        # Header
        header = tk.Frame(self.window, bg='#1a1a1a', height=60)
        header.pack(fill='x')
        tk.Label(header, text="QUANTUM MUSIC", font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='#00ff88').pack(expand=True)
        
        # Album art
        self.album_frame = tk.Frame(self.window, bg='#0a0a0a', height=150)
        self.album_frame.pack(fill='x', pady=10)
        
        self.album_canvas = tk.Canvas(self.album_frame, width=120, height=120, bg='#1a1a1a', highlightthickness=0)
        self.album_canvas.pack(pady=5)
        self.draw_album_art()
        
        # Track info
        self.track_info = tk.Label(self.window, text=self.tracks[self.current_track], 
                                 font=('Arial', 12, 'bold'), bg='#0a0a0a', fg='white')
        self.track_info.pack()
        
        # Controls
        controls = tk.Frame(self.window, bg='#0a0a0a')
        controls.pack(pady=10)
        
        tk.Button(controls, text="Previous", command=self.previous_track).pack(side='left', padx=5)
        self.play_btn = tk.Button(controls, text="Play", command=self.toggle_play, bg='#00aa00')
        self.play_btn.pack(side='left', padx=5)
        tk.Button(controls, text="Next", command=self.next_track).pack(side='left', padx=5)
        
        # Volume
        volume_frame = tk.Frame(self.window, bg='#0a0a0a')
        volume_frame.pack(pady=10)
        
        tk.Label(volume_frame, text="Volume:", font=('Arial', 10), 
                bg='#0a0a0a', fg='white').pack(side='left')
        
        self.volume_scale = tk.Scale(volume_frame, from_=0, to=100, orient='horizontal',
                                   bg='#0a0a0a', fg='white', highlightbackground='#0a0a0a')
        self.volume_scale.set(50)
        self.volume_scale.pack(side='left', padx=5)
        
        # Playlist
        playlist_frame = tk.Frame(self.window, bg='#0a0a0a')
        playlist_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        tk.Label(playlist_frame, text="Playlist:", font=('Arial', 10, 'bold'),
                bg='#0a0a0a', fg='#00ffff').pack(anchor='w')
        
        for i, track in enumerate(self.tracks):
            track_btn = tk.Button(playlist_frame, text=f"{i+1}. {track}", 
                                font=('Arial', 9), bg='#1a1a1a', fg='white',
                                command=lambda idx=i: self.select_track(idx))
            track_btn.pack(fill='x', pady=2)
    
    def draw_album_art(self):
        """ایجاد طرح آلبوم"""
        self.album_canvas.delete("all")
        w, h = 120, 120
        
        # ایجاد تصویر آلبوم
        img = Image.new('RGB', (w, h), color='#1a1a1a')
        draw = ImageDraw.Draw(img)
        
        # دایره مرکزی
        center_x, center_y = w//2, h//2
        draw.ellipse([center_x-40, center_y-40, center_x+40, center_y+40], fill='#00ff88')
        
        # خطوط چرخان
        for i in range(8):
            angle = time.time() * 2 + i * 0.785
            x1 = center_x + 30 * math.cos(angle)
            y1 = center_y + 30 * math.sin(angle)
            x2 = center_x + 50 * math.cos(angle)
            y2 = center_y + 50 * math.sin(angle)
            draw.line([x1, y1, x2, y2], fill='#ff44ff', width=3)
        
        # تبدیل به PhotoImage
        self.album_photo = ImageTk.PhotoImage(img)
        self.album_canvas.create_image(w//2, h//2, image=self.album_photo)
        
        if self.playing:
            self.window.after(100, self.draw_album_art)
    
    def toggle_play(self):
        """تغییر حالت پخش/توقف"""
        self.playing = not self.playing
        if self.playing:
            self.play_btn.config(text="Pause", bg='#ff8800')
            self.track_info.config(text=f"Playing: {self.tracks[self.current_track]}")
        else:
            self.play_btn.config(text="Play", bg='#00aa00')
            self.track_info.config(text=f"Paused: {self.tracks[self.current_track]}")
        
        self.draw_album_art()
    
    def previous_track(self):
        """ترک قبلی"""
        self.current_track = (self.current_track - 1) % len(self.tracks)
        self.track_info.config(text=self.tracks[self.current_track])
        if self.playing:
            self.draw_album_art()
    
    def next_track(self):
        """ترک بعدی"""
        self.current_track = (self.current_track + 1) % len(self.tracks)
        self.track_info.config(text=self.tracks[self.current_track])
        if self.playing:
            self.draw_album_art()
    
    def select_track(self, index):
        """انتخاب ترک خاص"""
        self.current_track = index
        self.track_info.config(text=self.tracks[self.current_track])
        if not self.playing:
            self.toggle_play()

class NeuralHealth:
    """سیستم سلامت عصبی"""
    def __init__(self, os):
        self.os = os
        self.window = None
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Neural Health Monitor")
        self.window.geometry("400x500")
        self.window.configure(bg='#0a0a0a')
        
        # Header
        header = tk.Frame(self.window, bg='#1a1a1a', height=60)
        header.pack(fill='x')
        tk.Label(header, text="NEURAL HEALTH", font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='#00ff88').pack(expand=True)
        
        # معیارهای سلامت
        metrics = [
            ("Heart Rate", "72", "BPM", "#ff4444"),
            ("Blood Pressure", "120/80", "mmHg", "#ff8844"), 
            ("Oxygen Level", "98", "%", "#4488ff"),
            ("Sleep Quality", "85", "%", "#8844ff"),
            ("Stress Level", "23", "%", "#ff44ff"),
            ("Mental Focus", "92", "%", "#44ff88")
        ]
        
        for name, value, unit, color in metrics:
            frame = tk.Frame(self.window, bg='#1a1a1a')
            frame.pack(fill='x', padx=20, pady=5)
            
            tk.Label(frame, text=name, font=('Arial', 12), bg='#1a1a1a', fg='white').pack(side='left')
            tk.Label(frame, text=f"{value} {unit}", font=('Arial', 14, 'bold'), 
                   bg='#1a1a1a', fg=color).pack(side='right')
        
        # نمودار سلامت
        self.health_canvas = tk.Canvas(self.window, width=360, height=150, bg='#1a1a1a', highlightthickness=0)
        self.health_canvas.pack(pady=20)
        self.draw_health_chart()
        
        # به روز رسانی خودکار
        self.update_health_data()
    
    def draw_health_chart(self):
        """رسم نمودار سلامت"""
        self.health_canvas.delete("all")
        
        # محورها
        self.health_canvas.create_line(30, 130, 330, 130, fill='#555555')  # محور X
        self.health_canvas.create_line(30, 130, 30, 30, fill='#555555')    # محور Y
        
        # داده‌های نمونه
        data = [random.randint(60, 100) for _ in range(7)]
        
        # رسم خط نمودار
        points = []
        for i, value in enumerate(data):
            x = 30 + i * 50
            y = 130 - value
            points.extend([x, y])
        
        if len(points) > 2:
            self.health_canvas.create_line(points, fill='#00ff88', width=2, smooth=True)
        
        # نقاط داده
        for i, value in enumerate(data):
            x = 30 + i * 50
            y = 130 - value
            self.health_canvas.create_oval(x-3, y-3, x+3, y+3, fill='#ff44ff', outline='')
    
    def update_health_data(self):
        """به روز رسانی داده‌های سلامت"""
        if self.window.winfo_exists():
            self.draw_health_chart()
            self.window.after(5000, self.update_health_data)

class QuantumFinance:
    """سیستم مالی کوانتومی"""
    def __init__(self, os):
        self.os = os
        self.window = None
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Quantum Finance")
        self.window.geometry("500x450")
        self.window.configure(bg='#0a0a0a')
        
        # Header
        header = tk.Frame(self.window, bg='#1a1a1a', height=60)
        header.pack(fill='x')
        tk.Label(header, text="QUANTUM FINANCE", font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='#ffff00').pack(expand=True)
        
        # ارزش پرتفوی
        portfolio_frame = tk.Frame(self.window, bg='#0a0a0a')
        portfolio_frame.pack(fill='x', padx=20, pady=10)
        
        self.portfolio_value = tk.Label(portfolio_frame, text="$154,832.47", 
                                      font=('Arial', 24, 'bold'), bg='#0a0a0a', fg='#00ff88')
        self.portfolio_value.pack()
        
        self.portfolio_change = tk.Label(portfolio_frame, text="+2.8% Today", 
                                       font=('Arial', 12), bg='#0a0a0a', fg='#00ff88')
        self.portfolio_change.pack()
        
        # شاخص‌های بازار
        indices_frame = tk.Frame(self.window, bg='#0a0a0a')
        indices_frame.pack(fill='x', padx=20, pady=10)
        
        indices = [
            ("QFI Index", "1,548.67", "+1.2%"),
            ("Quantum Tech", "845.23", "+2.8%"),
            ("Neural AI", "1,234.56", "+0.8%"),
            ("Crypto Assets", "23,456.78", "-0.5%")
        ]
        
        for name, value, change in indices:
            frame = tk.Frame(indices_frame, bg='#1a1a1a')
            frame.pack(fill='x', pady=2)
            
            tk.Label(frame, text=name, font=('Arial', 10), bg='#1a1a1a', fg='white').pack(side='left', padx=10)
            tk.Label(frame, text=value, font=('Arial', 10, 'bold'), bg='#1a1a1a', fg='#00ffff').pack(side='left')
            
            color = '#00ff88' if '+' in change else '#ff4444'
            tk.Label(frame, text=change, font=('Arial', 10), bg='#1a1a1a', fg=color).pack(side='right', padx=10)
        
        # نمودار قیمت
        self.chart_canvas = tk.Canvas(self.window, width=460, height=150, bg='#1a1a1a', highlightthickness=0)
        self.chart_canvas.pack(pady=10)
        self.draw_price_chart()
        
        # به روز رسانی خودکار
        self.update_finance_data()
    
    def draw_price_chart(self):
        """رسم نمودار قیمت"""
        self.chart_canvas.delete("all")
        
        # تولید داده‌های قیمت تصادفی
        prices = [100]
        for i in range(19):
            change = random.uniform(-5, 5)
            prices.append(max(50, prices[-1] + change))
        
        # مقیاس‌گذاری
        max_price = max(prices)
        min_price = min(prices)
        range_price = max_price - min_price
        
        if range_price == 0:
            range_price = 1
            
        points = []
        for i, price in enumerate(prices):
            x = 30 + i * 22
            y = 130 - ((price - min_price) / range_price) * 100
            points.extend([x, y])
        
        # رسم خط نمودار
        if len(points) > 2:
            self.chart_canvas.create_line(points, fill='#00ff88', width=2)
        
        # محورها
        self.chart_canvas.create_line(30, 130, 470, 130, fill='#555555')
        self.chart_canvas.create_line(30, 130, 30, 30, fill='#555555')
    
    def update_finance_data(self):
        """به روز رسانی داده‌های مالی"""
        # شبیه‌سازی تغییرات بازار
        if self.window.winfo_exists():
            self.draw_price_chart()
            self.window.after(3000, self.update_finance_data)

class SystemControl:
    """کنترل سیستم"""
    def __init__(self, os):
        self.os = os
        self.window = None
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("System Control")
        self.window.geometry("500x500")
        self.window.configure(bg='#0a0a0a')
        
        # Header
        header = tk.Frame(self.window, bg='#1a1a1a', height=60)
        header.pack(fill='x')
        tk.Label(header, text="SYSTEM CONTROL", font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='#ff4444').pack(expand=True)
        
        # وضعیت سیستم
        status_frame = tk.Frame(self.window, bg='#0a0a0a')
        status_frame.pack(fill='x', padx=20, pady=10)
        
        status_items = [
            ("CPU Usage", "23%", "#ff4444"),
            ("Memory", "65%", "#ff8844"), 
            ("Disk Space", "42%", "#ffff00"),
            ("Network", "1.2 Gbps", "#00ff88"),
            ("Temperature", "42°C", "#4488ff"),
            ("Battery", "87%", "#8844ff")
        ]
        
        for name, value, color in status_items:
            frame = tk.Frame(status_frame, bg='#1a1a1a')
            frame.pack(fill='x', pady=2)
            
            tk.Label(frame, text=name, font=('Arial', 11), bg='#1a1a1a', fg='white').pack(side='left', padx=10)
            tk.Label(frame, text=value, font=('Arial', 11, 'bold'), bg='#1a1a1a', fg=color).pack(side='right', padx=10)
        
        # کنترل‌های سیستم
        controls_frame = tk.Frame(self.window, bg='#0a0a0a')
        controls_frame.pack(fill='x', padx=20, pady=20)
        
        control_buttons = [
            ("Optimize System", self.optimize_system, '#00aa00'),
            ("Security Scan", self.security_scan, '#0088aa'),
            ("Clean Storage", self.clean_storage, '#8844ff'),
            ("Update System", self.update_system, '#ff8800'),
            ("Restart", self.restart_system, '#ff4444'),
            ("Shutdown", self.shutdown_system, '#aa0000')
        ]
        
        for i in range(0, len(control_buttons), 2):
            row_frame = tk.Frame(controls_frame, bg='#0a0a0a')
            row_frame.pack(fill='x', pady=5)
            
            for j in range(2):
                if i + j < len(control_buttons):
                    text, command, color = control_buttons[i + j]
                    btn = tk.Button(row_frame, text=text, font=('Arial', 10),
                                  bg=color, fg='white', width=15, height=2,
                                  command=command)
                    btn.pack(side='left', expand=True, padx=5)
        
        # لاگ سیستم
        log_frame = tk.Frame(self.window, bg='#0a0a0a')
        log_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        self.log_text = scrolledtext.ScrolledText(log_frame, height=8,
                                                bg='#1a1a1a', fg='#00ff88',
                                                font=('Arial', 9))
        self.log_text.pack(fill='both', expand=True)
        self.log_text.insert(tk.END, self.get_system_logs())
        self.log_text.config(state=tk.DISABLED)
    
    def optimize_system(self):
        self.add_log("System optimization started...")
        self.window.after(2000, lambda: self.add_log("System optimization completed!"))
    
    def security_scan(self):
        self.add_log("Security scan initiated...")
        self.window.after(1500, lambda: self.add_log("Security scan: No threats found"))
    
    def clean_storage(self):
        self.add_log("Storage cleanup in progress...")
        self.window.after(1000, lambda: self.add_log("Storage cleaned: 1.2GB freed"))
    
    def update_system(self):
        self.add_log("Checking for updates...")
        self.window.after(2000, lambda: self.add_log("System is up to date"))
    
    def restart_system(self):
        if messagebox.askyesno("Restart", "Restart system?"):
            self.add_log("System restart initiated...")
    
    def shutdown_system(self):
        if messagebox.askyesno("Shutdown", "Shutdown system?"):
            self.add_log("System shutdown initiated...")
    
    def add_log(self, message):
        """افزودن پیام به لاگ"""
        self.log_text.config(state=tk.NORMAL)
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.log_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)
    
    def get_system_logs(self):
        return """[SYSTEM] Quantum OS initialized
[NETWORK] All services running
[SECURITY] Firewall active
[PERFORMANCE] System optimal
"""

class ShutdownScreen:
    """صفحه خاموش کردن"""
    def __init__(self, os):
        self.os = os
        self.window = None
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Shutdown")
        self.window.geometry("300x200")
        self.window.configure(bg='#000000')
        
        tk.Label(self.window, text="SHUTDOWN", font=('Arial', 20, 'bold'),
                bg='#000000', fg='#ff4444').pack(expand=True)
        
        tk.Label(self.window, text="System is shutting down...", 
                font=('Arial', 12), bg='#000000', fg='#cccccc').pack()
        
        # شبیه‌سازی خاموش شدن
        self.window.after(3000, self.final_shutdown)
    
    def final_shutdown(self):
        self.window.destroy()
        self.os.root.quit()

# بازی حدس عدد
class NumberGuessingGame:
    """بازی حدس عدد"""
    def __init__(self, os):
        self.os = os
        self.window = None
        self.secret_number = 0
        self.attempts = 0
        self.max_attempts = 7
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Number Guessing Game")
        self.window.geometry("300x300")
        self.window.configure(bg='#0a0a0a')
        
        # Header
        header = tk.Frame(self.window, bg='#1a1a1a', height=50)
        header.pack(fill='x')
        tk.Label(header, text="GUESS THE NUMBER", font=('Arial', 14, 'bold'),
                bg='#1a1a1a', fg='#00ffff').pack(expand=True)
        
        # شروع بازی جدید
        self.new_game()
        
        # ورودی کاربر
        input_frame = tk.Frame(self.window, bg='#0a0a0a')
        input_frame.pack(pady=20)
        
        tk.Label(input_frame, text="Enter your guess (1-100):", 
                font=('Arial', 10), bg='#0a0a0a', fg='white').pack()
        
        self.guess_entry = tk.Entry(input_frame, font=('Arial', 14), width=10)
        self.guess_entry.pack(pady=5)
        self.guess_entry.bind('<Return>', self.check_guess)
        
        tk.Button(input_frame, text="Guess", font=('Arial', 12),
                 bg='#00aa00', fg='white', command=self.check_guess).pack(pady=5)
        
        # نمایش نتیجه
        self.result_label = tk.Label(self.window, text=f"Guess a number between 1 and 100!\nYou have {self.max_attempts} attempts.",
                                   font=('Arial', 10), bg='#0a0a0a', fg='#00ff88', justify='center')
        self.result_label.pack(pady=10)
        
        # دکمه بازی جدید
        tk.Button(self.window, text="New Game", font=('Arial', 10),
                 bg='#0088aa', fg='white', command=self.new_game).pack(pady=10)
    
    def new_game(self):
        """شروع بازی جدید"""
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        if hasattr(self, 'result_label'):
            self.result_label.config(text=f"New game started! Guess a number between 1 and 100.\nYou have {self.max_attempts} attempts.")
        if hasattr(self, 'guess_entry'):
            self.guess_entry.delete(0, tk.END)
    
    def check_guess(self, event=None):
        """بررسی حدس کاربر"""
        try:
            guess = int(self.guess_entry.get())
            self.attempts += 1
            
            if guess < self.secret_number:
                self.result_label.config(text=f"Too low! Try higher.\nAttempts: {self.attempts}/{self.max_attempts}", fg='#ff4444')
            elif guess > self.secret_number:
                self.result_label.config(text=f"Too high! Try lower.\nAttempts: {self.attempts}/{self.max_attempts}", fg='#ff8844')
            else:
                self.result_label.config(text=f"Congratulations! You won!\nThe number was {self.secret_number}.\nAttempts: {self.attempts}", fg='#00ff88')
                return
            
            if self.attempts >= self.max_attempts:
                self.result_label.config(text=f"Game over! The number was {self.secret_number}.", fg='#ff4444')
            
            self.guess_entry.delete(0, tk.END)
            
        except ValueError:
            self.result_label.config(text="Please enter a valid number!", fg='#ff4444')

# بازی دوز (Tic-Tac-Toe)
class TicTacToeGame:
    """بازی دوز"""
    def __init__(self, os):
        self.os = os
        self.window = None
        self.board = ['' for _ in range(9)]
        self.current_player = 'X'
        self.game_over = False
        
    def show(self):
        self.window = tk.Toplevel(self.os.root)
        self.window.title("Tic-Tac-Toe")
        self.window.geometry("300x350")
        self.window.configure(bg='#0a0a0a')
        
        # Header
        header = tk.Frame(self.window, bg='#1a1a1a', height=50)
        header.pack(fill='x')
        tk.Label(header, text="TIC-TAC-TOE", font=('Arial', 16, 'bold'),
                bg='#1a1a1a', fg='#00ffff').pack(expand=True)
        
        # نمایش بازیکن فعلی
        self.status_label = tk.Label(self.window, text=f"Player {self.current_player}'s turn",
                                   font=('Arial', 12, 'bold'), bg='#0a0a0a', fg='#00ff88')
        self.status_label.pack(pady=10)
        
        # صفحه بازی
        self.board_frame = tk.Frame(self.window, bg='#0a0a0a')
        self.board_frame.pack(pady=10)
        
        self.buttons = []
        for i in range(9):
            btn = tk.Button(self.board_frame, text='', font=('Arial', 20, 'bold'),
                          width=3, height=1, bg='#1a1a1a', fg='white',
                          command=lambda idx=i: self.make_move(idx))
            row, col = i // 3, i % 3
            btn.grid(row=row, column=col, padx=2, pady=2)
            self.buttons.append(btn)
        
        # دکمه بازی جدید
        tk.Button(self.window, text="New Game", font=('Arial', 12),
                 bg='#0088aa', fg='white', command=self.new_game).pack(pady=10)
    
    def make_move(self, position):
        """انجام حرکت"""
        if not self.game_over and self.board[position] == '':
            self.board[position] = self.current_player
            self.buttons[position].config(text=self.current_player, 
                                        fg='#ff4444' if self.current_player == 'X' else '#4488ff')
            
            if self.check_winner():
                self.status_label.config(text=f"Player {self.current_player} wins!", fg='#00ff88')
                self.game_over = True
            elif '' not in self.board:
                self.status_label.config(text="It's a tie!", fg='#ffff00')
                self.game_over = True
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.status_label.config(text=f"Player {self.current_player}'s turn")
    
    def check_winner(self):
        """بررسی برنده"""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # ردیف‌ها
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # ستون‌ها
            [0, 4, 8], [2, 4, 6]              # مورب‌ها
        ]
        
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == 
                self.board[combo[2]] == self.current_player):
                for pos in combo:
                    self.buttons[pos].config(bg='#005500')
                return True
        return False
    
    def new_game(self):
        """شروع بازی جدید"""
        self.board = ['' for _ in range(9)]
        self.current_player = 'X'
        self.game_over = False
        
        for btn in self.buttons:
            btn.config(text='', bg='#1a1a1a')
        
        self.status_label.config(text=f"Player {self.current_player}'s turn", fg='#00ff88')

if __name__ == "__main__":
    print("QUANTUM OS INITIALIZATION SEQUENCE")
    print("QUANTUM CORE: ACTIVATED")
    print("NEURAL NETWORKS: ONLINE")
    print("QUANTUM ENTANGLEMENT: STABLE")
    print("TEMPORAL SYNCHRONIZATION: OPTIMAL")
    print("FILE SYSTEM: READY")
    print("ALL SYSTEMS: READY")
    
    quantum_os = QuantumMobileOS()
    quantum_os.run()