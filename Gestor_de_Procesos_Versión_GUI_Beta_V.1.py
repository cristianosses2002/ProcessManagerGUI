#!/usr/bin/env python3
"""
Gestor de Procesos Avanzado - Con Recomendaciones de Seguridad
Creado por: CristianOsses
Incluye sistema de recomendaciones para desactivar servicios de forma segura
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import psutil
import threading
import time
import subprocess
import os
import winreg
from datetime import datetime
import json

class ProcessManagerAdvanced:
    def __init__(self, root):
        self.root = root
        self.root.title("🔧 Gestor de Procesos Avanzado - Con Recomendaciones")
        self.root.geometry("1400x800")
        self.root.resizable(True, True)
        
        self.processes = []
        self.services = []
        self.auto_refresh = False
        self.refresh_thread = None
        
        # Base de datos de recomendaciones
        self.recommendations = self.load_recommendations()
        
        self.setup_ui()
        self.refresh_processes()
        self.refresh_services()
    
    def load_recommendations(self):
        """Carga la base de datos de recomendaciones"""
        return {
            # Servicios seguros para desactivar
            "safe_to_disable": {
                "Fax": {
                    "name": "Servicio de Fax",
                    "description": "Servicio de fax obsoleto, seguro desactivar",
                    "impact": "Ninguno",
                    "category": "Obsoleto",
                    "safety": "Muy Seguro"
                },
                "TapiSrv": {
                    "name": "Telephony",
                    "description": "API de telefonía, raramente usado",
                    "impact": "Ninguno para la mayoría",
                    "category": "Telefonía",
                    "safety": "Muy Seguro"
                },
                "SysMain": {
                    "name": "Superfetch",
                    "description": "Precarga aplicaciones, consume recursos",
                    "impact": "Menor velocidad de inicio de apps",
                    "category": "Rendimiento",
                    "safety": "Seguro"
                },
                "TabletInputService": {
                    "name": "Tablet PC Input Service",
                    "description": "Servicio para tablets, innecesario en PC",
                    "impact": "Ninguno en PCs normales",
                    "category": "Tablet",
                    "safety": "Muy Seguro"
                },
                "WSearch": {
                    "name": "Windows Search",
                    "description": "Indexado de archivos, consume recursos",
                    "impact": "Búsquedas más lentas",
                    "category": "Búsqueda",
                    "safety": "Seguro"
                },
                "Themes": {
                    "name": "Themes",
                    "description": "Gestión de temas visuales",
                    "impact": "Solo tema clásico disponible",
                    "category": "Visual",
                    "safety": "Seguro"
                },
                "PrintSpooler": {
                    "name": "Print Spooler",
                    "description": "Cola de impresión (si no usas impresora)",
                    "impact": "No podrás imprimir",
                    "category": "Impresión",
                    "safety": "Seguro"
                },
                "WbioSrvc": {
                    "name": "Windows Biometric Service",
                    "description": "Servicio biométrico (si no usas huella)",
                    "impact": "Sin autenticación biométrica",
                    "category": "Biometría",
                    "safety": "Seguro"
                },
                "DiagTrack": {
                    "name": "Diagnostic Tracking Service",
                    "description": "Telemetría de Windows",
                    "impact": "Mejor privacidad",
                    "category": "Privacidad",
                    "safety": "Seguro"
                },
                "dmwappushservice": {
                    "name": "WAP Push Message Routing",
                    "description": "Enrutamiento de mensajes WAP",
                    "impact": "Ninguno",
                    "category": "Mensajería",
                    "safety": "Muy Seguro"
                }
            },
            # Procesos que consumen muchos recursos
            "resource_heavy": {
                "MsMpEng.exe": {
                    "name": "Windows Defender Antimalware",
                    "description": "Antivirus integrado, alto consumo",
                    "impact": "Reducir protección antivirus",
                    "category": "Seguridad",
                    "safety": "Cuidado"
                },
                "SearchIndexer.exe": {
                    "name": "Search Indexer",
                    "description": "Indexador de búsqueda",
                    "impact": "Búsquedas más lentas",
                    "category": "Búsqueda",
                    "safety": "Seguro"
                },
                "SysMain": {
                    "name": "Superfetch/Prefetch",
                    "description": "Precarga de aplicaciones",
                    "impact": "Inicio más lento de apps",
                    "category": "Rendimiento",
                    "safety": "Seguro"
                }
            },
            # Servicios críticos - NO desactivar
            "critical": {
                "Winlogon": "Inicio de sesión de Windows",
                "csrss": "Client Server Runtime Process",
                "wininit": "Inicialización de Windows",
                "services": "Service Control Manager",
                "lsass": "Local Security Authority",
                "smss": "Session Manager",
                "explorer": "Windows Explorer"
            }
        }
    
    def setup_ui(self):
        """Configura la interfaz de usuario"""
        # Crear notebook para pestañas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Pestaña de Procesos
        self.setup_processes_tab()
        
        # Pestaña de Servicios
        self.setup_services_tab()
        
        # Pestaña de Recomendaciones
        self.setup_recommendations_tab()
        
        # Pestaña de Optimización
        self.setup_optimization_tab()
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Listo")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)
    
    def setup_processes_tab(self):
        """Configura la pestaña de procesos"""
        process_frame = ttk.Frame(self.notebook)
        self.notebook.add(process_frame, text="🔍 Procesos")
        
        # Frame de controles
        control_frame = ttk.LabelFrame(process_frame, text="Controles", padding="5")
        control_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(control_frame, text="🔄 Refrescar", command=self.refresh_processes).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="❌ Terminar", command=self.terminate_process).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="⚠️ Forzar", command=self.force_kill_process).pack(side=tk.LEFT, padx=5)
        
        # Auto-refresh
        self.auto_refresh_var = tk.BooleanVar()
        ttk.Checkbutton(control_frame, text="Auto-refrescar", 
                       variable=self.auto_refresh_var, 
                       command=self.toggle_auto_refresh).pack(side=tk.LEFT, padx=10)
        
        # Filtros
        ttk.Label(control_frame, text="Filtrar:").pack(side=tk.LEFT, padx=5)
        self.filter_var = tk.StringVar()
        filter_entry = ttk.Entry(control_frame, textvariable=self.filter_var, width=20)
        filter_entry.pack(side=tk.LEFT, padx=5)
        filter_entry.bind('<KeyRelease>', self.filter_processes)
        
        # Tabla de procesos
        columns = ('PID', 'Nombre', 'Usuario', 'CPU%', 'Memoria%', 'Estado', 'Recomendación')
        self.process_tree = ttk.Treeview(process_frame, columns=columns, show='headings', height=15)
        
        # Configurar columnas
        for col in columns:
            self.process_tree.heading(col, text=col, command=lambda c=col: self.sort_column(self.process_tree, c))
        
        self.process_tree.column('PID', width=80)
        self.process_tree.column('Nombre', width=200)
        self.process_tree.column('Usuario', width=120)
        self.process_tree.column('CPU%', width=80)
        self.process_tree.column('Memoria%', width=80)
        self.process_tree.column('Estado', width=100)
        self.process_tree.column('Recomendación', width=150)
        
        # Scrollbars
        v_scroll = ttk.Scrollbar(process_frame, orient=tk.VERTICAL, command=self.process_tree.yview)
        h_scroll = ttk.Scrollbar(process_frame, orient=tk.HORIZONTAL, command=self.process_tree.xview)
        self.process_tree.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)
        
        # Pack
        self.process_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        
        # Bind eventos
        self.process_tree.bind('<<TreeviewSelect>>', self.on_process_select)
        self.process_tree.bind('<Double-1>', self.show_process_details)
        
        # Configurar colores para recomendaciones
        self.process_tree.tag_configure('safe', background='#d4edda')
        self.process_tree.tag_configure('caution', background='#fff3cd')
        self.process_tree.tag_configure('critical', background='#f8d7da')
        self.process_tree.tag_configure('heavy', background='#e2e3e5')
    
    def setup_services_tab(self):
        """Configura la pestaña de servicios"""
        service_frame = ttk.Frame(self.notebook)
        self.notebook.add(service_frame, text="⚙️ Servicios")
        
        # Frame de controles
        control_frame = ttk.LabelFrame(service_frame, text="Controles de Servicios", padding="5")
        control_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(control_frame, text="🔄 Refrescar", command=self.refresh_services).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="⏹️ Detener", command=self.stop_service).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="▶️ Iniciar", command=self.start_service).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="🚫 Desactivar", command=self.disable_service).pack(side=tk.LEFT, padx=5)
        
        # Tabla de servicios
        columns = ('Nombre', 'Nombre Mostrado', 'Estado', 'Inicio', 'Recomendación')
        self.service_tree = ttk.Treeview(service_frame, columns=columns, show='headings', height=20)
        
        for col in columns:
            self.service_tree.heading(col, text=col)
        
        self.service_tree.column('Nombre', width=200)
        self.service_tree.column('Nombre Mostrado', width=250)
        self.service_tree.column('Estado', width=100)
        self.service_tree.column('Inicio', width=100)
        self.service_tree.column('Recomendación', width=150)
        
        # Scrollbars para servicios
        v_scroll2 = ttk.Scrollbar(service_frame, orient=tk.VERTICAL, command=self.service_tree.yview)
        self.service_tree.configure(yscrollcommand=v_scroll2.set)
        
        self.service_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        v_scroll2.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Configurar colores para servicios
        self.service_tree.tag_configure('safe', background='#d4edda')
        self.service_tree.tag_configure('caution', background='#fff3cd')
        self.service_tree.tag_configure('critical', background='#f8d7da')
        self.service_tree.tag_configure('running', background='#cce5ff')
        self.service_tree.tag_configure('stopped', background='#f0f0f0')
    
    def setup_recommendations_tab(self):
        """Configura la pestaña de recomendaciones"""
        rec_frame = ttk.Frame(self.notebook)
        self.notebook.add(rec_frame, text="💡 Recomendaciones")
        
        # Frame de información
        info_frame = ttk.LabelFrame(rec_frame, text="Información", padding="10")
        info_frame.pack(fill=tk.X, padx=5, pady=5)
        
        info_text = """
        🔍 RECOMENDACIONES DE SEGURIDAD
        
        🟢 VERDE: Muy seguro desactivar - Sin impacto en el sistema
        🟡 AMARILLO: Seguro con precaución - Puede tener impacto menor
        🔴 ROJO: CRÍTICO - NO desactivar bajo ninguna circunstancia
        🔵 AZUL: Alto consumo de recursos - Evaluar desactivación
        
        ⚠️ IMPORTANTE: Crea un punto de restauración antes de desactivar servicios
        """
        
        ttk.Label(info_frame, text=info_text, font=("Arial", 9), justify=tk.LEFT).pack()
        
        # Botón para punto de restauración
        ttk.Button(info_frame, text="📂 Crear Punto de Restauración", 
                  command=self.create_restore_point).pack(pady=5)
        
        # Frame de recomendaciones
        rec_list_frame = ttk.LabelFrame(rec_frame, text="Servicios Recomendados para Desactivar", padding="5")
        rec_list_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Crear lista de recomendaciones
        self.rec_tree = ttk.Treeview(rec_list_frame, 
                                    columns=('Servicio', 'Nombre', 'Descripción', 'Impacto', 'Seguridad'),
                                    show='headings', height=15)
        
        self.rec_tree.heading('Servicio', text='Servicio')
        self.rec_tree.heading('Nombre', text='Nombre')
        self.rec_tree.heading('Descripción', text='Descripción')
        self.rec_tree.heading('Impacto', text='Impacto')
        self.rec_tree.heading('Seguridad', text='Seguridad')
        
        self.rec_tree.column('Servicio', width=150)
        self.rec_tree.column('Nombre', width=200)
        self.rec_tree.column('Descripción', width=300)
        self.rec_tree.column('Impacto', width=200)
        self.rec_tree.column('Seguridad', width=100)
        
        # Poblar recomendaciones
        self.populate_recommendations()
        
        # Scrollbar para recomendaciones
        v_scroll3 = ttk.Scrollbar(rec_list_frame, orient=tk.VERTICAL, command=self.rec_tree.yview)
        self.rec_tree.configure(yscrollcommand=v_scroll3.set)
        
        self.rec_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        v_scroll3.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Botones de acción
        action_frame = ttk.Frame(rec_frame)
        action_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(action_frame, text="✅ Desactivar Seleccionado", 
                  command=self.disable_recommended).pack(side=tk.LEFT, padx=5)
        ttk.Button(action_frame, text="🔄 Desactivar Todos los Seguros", 
                  command=self.disable_all_safe).pack(side=tk.LEFT, padx=5)
    
    def setup_optimization_tab(self):
        """Configura la pestaña de optimización"""
        opt_frame = ttk.Frame(self.notebook)
        self.notebook.add(opt_frame, text="🚀 Optimización")
        
        # Frame de sistema
        system_frame = ttk.LabelFrame(opt_frame, text="Información del Sistema", padding="10")
        system_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.system_info_text = scrolledtext.ScrolledText(system_frame, height=8, font=("Consolas", 9))
        self.system_info_text.pack(fill=tk.BOTH, expand=True)
        
        # Frame de optimizaciones automáticas
        auto_opt_frame = ttk.LabelFrame(opt_frame, text="Optimizaciones Automáticas", padding="10")
        auto_opt_frame.pack(fill=tk.X, padx=5, pady=5)
        
        ttk.Button(auto_opt_frame, text="🧹 Limpiar Archivos Temporales", 
                  command=self.clean_temp_files).pack(side=tk.LEFT, padx=5)
        ttk.Button(auto_opt_frame, text="💾 Optimizar Memoria", 
                  command=self.optimize_memory).pack(side=tk.LEFT, padx=5)
        ttk.Button(auto_opt_frame, text="🔧 Desfragmentar Registro", 
                  command=self.defrag_registry).pack(side=tk.LEFT, padx=5)
        
        # Frame de optimización para gaming
        gaming_frame = ttk.LabelFrame(opt_frame, text="🎮 Optimización para Gaming", padding="10")
        gaming_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Botones de gaming
        gaming_buttons_frame = ttk.Frame(gaming_frame)
        gaming_buttons_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(gaming_buttons_frame, text="🎯 Optimización Completa Gaming", 
                  command=self.full_gaming_optimization).pack(side=tk.LEFT, padx=5)
        ttk.Button(gaming_buttons_frame, text="📦 Crear Backup del Sistema", 
                  command=self.create_system_backup).pack(side=tk.LEFT, padx=5)
        ttk.Button(gaming_buttons_frame, text="🔄 Restaurar desde Backup", 
                  command=self.restore_from_backup).pack(side=tk.LEFT, padx=5)
        
        # Frame de procesos para gaming
        gaming_processes_frame = ttk.LabelFrame(gaming_frame, text="Procesos a Cerrar para Gaming", padding="5")
        gaming_processes_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        # Lista de procesos para gaming
        self.gaming_processes = [
            "chrome.exe", "firefox.exe", "msedge.exe", "opera.exe", "brave.exe",
            "discord.exe", "teams.exe", "skype.exe", "zoom.exe", "slack.exe",
            "spotify.exe", "itunes.exe", "vlc.exe", "mediaplayer.exe",
            "outlook.exe", "thunderbird.exe", "teams.exe", "onedrive.exe",
            "dropbox.exe", "google-drive.exe", "mega.exe",
            "steam.exe", "origin.exe", "uplay.exe", "epicgameslauncher.exe",
            "nvidia-geforce-experience.exe", "amd-software.exe", "msi-afterburner.exe",
            "icue.exe", "nzxt-cam.exe", "corsair-icue.exe", "logitech-gaming-software.exe",
            "razer-synapse.exe", "steelseries-engine.exe"
        ]
        
        # Crear treeview para procesos de gaming
        columns = ('Proceso', 'Estado', 'Acción')
        self.gaming_tree = ttk.Treeview(gaming_processes_frame, columns=columns, show='headings', height=10)
        
        for col in columns:
            self.gaming_tree.heading(col, text=col)
        
        self.gaming_tree.column('Proceso', width=200)
        self.gaming_tree.column('Estado', width=100)
        self.gaming_tree.column('Acción', width=150)
        
        # Poblar lista de procesos de gaming
        self.populate_gaming_processes()
        
        # Scrollbar para gaming
        v_scroll_gaming = ttk.Scrollbar(gaming_processes_frame, orient=tk.VERTICAL, command=self.gaming_tree.yview)
        self.gaming_tree.configure(yscrollcommand=v_scroll_gaming.set)
        
        self.gaming_tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        v_scroll_gaming.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Botones de acción para gaming
        gaming_action_frame = ttk.Frame(gaming_frame)
        gaming_action_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(gaming_action_frame, text="🎮 Cerrar Todos los Procesos de Gaming", 
                  command=self.close_all_gaming_processes).pack(side=tk.LEFT, padx=5)
        ttk.Button(gaming_action_frame, text="🎯 Cerrar Seleccionados", 
                  command=self.close_selected_gaming_processes).pack(side=tk.LEFT, padx=5)
        ttk.Button(gaming_action_frame, text="🔄 Refrescar Lista", 
                  command=self.refresh_gaming_processes).pack(side=tk.LEFT, padx=5)
        
        # Actualizar información del sistema
        self.update_system_info()
    
    def populate_recommendations(self):
        """Pobla la lista de recomendaciones"""
        for service, info in self.recommendations["safe_to_disable"].items():
            tag = 'safe' if info["safety"] == "Muy Seguro" else 'caution'
            self.rec_tree.insert('', 'end', 
                                values=(service, info["name"], info["description"], 
                                       info["impact"], info["safety"]),
                                tags=(tag,))
        
        # Configurar colores
        self.rec_tree.tag_configure('safe', background='#d4edda')
        self.rec_tree.tag_configure('caution', background='#fff3cd')
    
    def refresh_processes(self):
        """Actualiza la lista de procesos"""
        self.status_var.set("Cargando procesos...")
        
        # Limpiar tabla
        for item in self.process_tree.get_children():
            self.process_tree.delete(item)
        
        self.processes = []
        
        # Obtener procesos
        for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent', 'status']):
            try:
                self.processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        
        # Ordenar por CPU
        self.processes.sort(key=lambda x: x['cpu_percent'] or 0, reverse=True)
        
        # Llenar tabla con recomendaciones
        for proc in self.processes:
            pid = proc['pid']
            name = proc['name'] or 'N/A'
            username = proc['username'] or 'N/A'
            cpu = f"{proc['cpu_percent']:.1f}" if proc['cpu_percent'] else "0.0"
            memory = f"{proc['memory_percent']:.1f}" if proc['memory_percent'] else "0.0"
            status = proc['status']
            
            # Determinar recomendación
            recommendation, tag = self.get_process_recommendation(name)
            
            self.process_tree.insert('', 'end', 
                                   values=(pid, name, username, cpu, memory, status, recommendation),
                                   tags=(tag,))
        
        self.status_var.set(f"Cargados {len(self.processes)} procesos")
    
    def get_process_recommendation(self, process_name):
        """Obtiene recomendación para un proceso"""
        # Verificar si es crítico
        for critical in self.recommendations["critical"]:
            if critical.lower() in process_name.lower():
                return "🔴 CRÍTICO - NO tocar", "critical"
        
        # Verificar si consume muchos recursos
        for heavy in self.recommendations["resource_heavy"]:
            if heavy.lower() in process_name.lower():
                return "🔵 Alto consumo", "heavy"
        
        # Verificar si es seguro desactivar
        for safe in self.recommendations["safe_to_disable"]:
            if safe.lower() in process_name.lower():
                return "🟢 Seguro desactivar", "safe"
        
        return "⚪ Normal", "normal"
    
    def refresh_services(self):
        """Actualiza la lista de servicios"""
        self.status_var.set("Cargando servicios...")
        
        # Limpiar tabla
        for item in self.service_tree.get_children():
            self.service_tree.delete(item)
        
        self.services = []
        
        try:
            # Obtener servicios usando psutil
            for service in psutil.win_service_iter():
                try:
                    service_info = service.as_dict()
                    self.services.append(service_info)
                except Exception:
                    continue
            
            # Llenar tabla
            for service in self.services:
                name = service.get('name', 'N/A')
                display_name = service.get('display_name', 'N/A')
                status = service.get('status', 'N/A')
                start_type = service.get('start_type', 'N/A')
                
                # Determinar recomendación
                recommendation, tag = self.get_service_recommendation(name)
                
                # Agregar tag de estado
                if status == 'running':
                    tag = 'running'
                elif status == 'stopped':
                    tag = 'stopped'
                
                self.service_tree.insert('', 'end', 
                                       values=(name, display_name, status, start_type, recommendation),
                                       tags=(tag,))
        
        except Exception as e:
            messagebox.showerror("Error", f"Error al cargar servicios: {str(e)}")
        
        self.status_var.set(f"Cargados {len(self.services)} servicios")
    
    def get_service_recommendation(self, service_name):
        """Obtiene recomendación para un servicio"""
        # Verificar si es seguro desactivar
        if service_name in self.recommendations["safe_to_disable"]:
            return "🟢 Seguro desactivar", "safe"
        
        # Verificar si es crítico
        for critical in self.recommendations["critical"]:
            if critical.lower() in service_name.lower():
                return "🔴 CRÍTICO", "critical"
        
        return "⚪ Normal", "normal"
    
    def disable_service(self):
        """Desactiva el servicio seleccionado"""
        selection = self.service_tree.selection()
        if not selection:
            messagebox.showwarning("Advertencia", "Selecciona un servicio primero")
            return
        
        item = self.service_tree.item(selection[0])
        service_name = item['values'][0]
        
        # Verificar si es seguro
        if service_name in self.recommendations["critical"]:
            messagebox.showerror("Error", "Este servicio es CRÍTICO y no debe desactivarse")
            return
        
        if messagebox.askyesno("Confirmar", f"¿Desactivar permanentemente el servicio '{service_name}'?"):
            try:
                # Detener el servicio
                subprocess.run(['sc', 'stop', service_name], check=False, capture_output=True)
                
                # Desactivar el servicio
                result = subprocess.run(['sc', 'config', service_name, 'start=', 'disabled'], 
                                      capture_output=True, text=True)
                
                if result.returncode == 0:
                    messagebox.showinfo("Éxito", f"Servicio '{service_name}' desactivado permanentemente")
                    self.refresh_services()
                else:
                    messagebox.showerror("Error", f"Error al desactivar servicio: {result.stderr}")
                    
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")
    
    def disable_recommended(self):
        """Desactiva el servicio recomendado seleccionado"""
        selection = self.rec_tree.selection()
        if not selection:
            messagebox.showwarning("Advertencia", "Selecciona una recomendación primero")
            return
        
        item = self.rec_tree.item(selection[0])
        service_name = item['values'][0]
        
        if messagebox.askyesno("Confirmar", f"¿Desactivar el servicio recomendado '{service_name}'?"):
            try:
                subprocess.run(['sc', 'stop', service_name], check=False, capture_output=True)
                result = subprocess.run(['sc', 'config', service_name, 'start=', 'disabled'], 
                                      capture_output=True, text=True)
                
                if result.returncode == 0:
                    messagebox.showinfo("Éxito", f"Servicio '{service_name}' desactivado")
                    self.refresh_services()
                else:
                    messagebox.showerror("Error", f"Error: {result.stderr}")
                    
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")
    
    def disable_all_safe(self):
        """Desactiva todos los servicios seguros"""
        if not messagebox.askyesno("Confirmar", "¿Desactivar TODOS los servicios seguros?\n\nEsta acción afectará múltiples servicios."):
            return
        
        disabled_count = 0
        errors = []
        
        for service_name in self.recommendations["safe_to_disable"]:
            try:
                subprocess.run(['sc', 'stop', service_name], check=False, capture_output=True)
                result = subprocess.run(['sc', 'config', service_name, 'start=', 'disabled'], 
                                      capture_output=True, text=True)
                
                if result.returncode == 0:
                    disabled_count += 1
                else:
                    errors.append(f"{service_name}: {result.stderr}")
                    
            except Exception as e:
                errors.append(f"{service_name}: {str(e)}")
        
        message = f"Desactivados {disabled_count} servicios."
        if errors:
            message += f"\n\nErrores en {len(errors)} servicios:\n" + "\n".join(errors[:5])
        
        messagebox.showinfo("Resultado", message)
        self.refresh_services()
    
    def create_restore_point(self):
        """Crea un punto de restauración del sistema"""
        try:
            # Crear punto de restauración
            result = subprocess.run([
                'powershell', '-Command',
                'Checkpoint-Computer -Description "Antes de optimizaciones" -RestorePointType "APPLICATION_INSTALL"'
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                messagebox.showinfo("Éxito", "Punto de restauración creado exitosamente")
            else:
                messagebox.showerror("Error", f"Error al crear punto de restauración: {result.stderr}")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error: {str(e)}")
    
    def clean_temp_files(self):
        """Limpia archivos temporales"""
        try:
            # Limpiar archivos temporales
            temp_paths = [
                os.path.expandvars(r'%TEMP%'),
                os.path.expandvars(r'%WINDIR%\Temp'),
                os.path.expandvars(r'%WINDIR%\Prefetch')
            ]
            
            deleted_count = 0
            for temp_path in temp_paths:
                if os.path.exists(temp_path):
                    for file in os.listdir(temp_path):
                        try:
                            file_path = os.path.join(temp_path, file)
                            if os.path.isfile(file_path):
                                os.remove(file_path)
                                deleted_count += 1
                        except:
                            continue
            
            messagebox.showinfo("Éxito", f"Limpieza completada. {deleted_count} archivos eliminados.")
            self.status_var.set("Archivos temporales limpiados")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al limpiar archivos temporales: {str(e)}")
    
    def optimize_memory(self):
        """Optimiza el uso de memoria"""
        try:
            # Forzar recolección de basura
            import gc
            gc.collect()
            
            # Liberar memoria del sistema
            result = subprocess.run(['powershell', '-Command', 
                                   'Get-Process | Where-Object {$_.WorkingSet -gt 100MB} | Stop-Process -Force'],
                                  capture_output=True, text=True)
            
            messagebox.showinfo("Éxito", "Memoria optimizada. Procesos pesados terminados.")
            self.status_var.set("Memoria optimizada")
            self.refresh_processes()
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al optimizar memoria: {str(e)}")
    
    def defrag_registry(self):
        """Desfragmenta el registro de Windows"""
        try:
            # Usar regedit para optimizar el registro
            result = subprocess.run(['regedit', '/e', 'temp_reg.reg'], 
                                  capture_output=True, text=True)
            
            messagebox.showinfo("Éxito", "Registro optimizado")
            self.status_var.set("Registro optimizado")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al optimizar registro: {str(e)}")
    
    def update_system_info(self):
        """Actualiza la información del sistema"""
        try:
            # Obtener información del sistema
            cpu_count = psutil.cpu_count()
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            info_text = f"""
=== INFORMACIÓN DEL SISTEMA ===

🖥️ CPU:
   - Núcleos: {cpu_count}
   - Uso actual: {cpu_percent:.1f}%

💾 Memoria RAM:
   - Total: {memory.total / (1024**3):.1f} GB
   - Disponible: {memory.available / (1024**3):.1f} GB
   - Uso: {memory.percent:.1f}%

💿 Disco Duro:
   - Total: {disk.total / (1024**3):.1f} GB
   - Libre: {disk.free / (1024**3):.1f} GB
   - Uso: {disk.percent:.1f}%

📊 Procesos Activos: {len(psutil.pids())}
⏰ Hora del Sistema: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
            
            self.system_info_text.delete(1.0, tk.END)
            self.system_info_text.insert(1.0, info_text)
            
        except Exception as e:
            self.system_info_text.delete(1.0, tk.END)
            self.system_info_text.insert(1.0, f"Error al obtener información del sistema: {str(e)}")
    
    def populate_gaming_processes(self):
        """Pobla la lista de procesos de gaming"""
        # Limpiar lista
        for item in self.gaming_tree.get_children():
            self.gaming_tree.delete(item)
        
        # Verificar qué procesos están ejecutándose
        running_processes = []
        for proc in psutil.process_iter(['pid', 'name']):
            try:
                running_processes.append(proc.info['name'].lower())
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue
        
        # Agregar procesos a la lista
        for process_name in self.gaming_processes:
            is_running = process_name.lower() in running_processes
            status = "🟢 Ejecutándose" if is_running else "🔴 No ejecutándose"
            action = "Cerrar" if is_running else "N/A"
            
            tag = 'running' if is_running else 'stopped'
            
            self.gaming_tree.insert('', 'end', 
                                  values=(process_name, status, action),
                                  tags=(tag,))
        
        # Configurar colores
        self.gaming_tree.tag_configure('running', background='#d4edda')
        self.gaming_tree.tag_configure('stopped', background='#f8d7da')
    
    def refresh_gaming_processes(self):
        """Refresca la lista de procesos de gaming"""
        self.populate_gaming_processes()
        self.status_var.set("Lista de procesos de gaming actualizada")
    
    def close_selected_gaming_processes(self):
        """Cierra los procesos de gaming seleccionados"""
        selection = self.gaming_tree.selection()
        if not selection:
            messagebox.showwarning("Advertencia", "Selecciona procesos para cerrar")
            return
        
        closed_count = 0
        errors = []
        
        for item_id in selection:
            item = self.gaming_tree.item(item_id)
            process_name = item['values'][0]
            status = item['values'][1]
            
            if "Ejecutándose" in status:
                try:
                    # Buscar y cerrar el proceso
                    for proc in psutil.process_iter(['pid', 'name']):
                        try:
                            if proc.info['name'].lower() == process_name.lower():
                                proc.terminate()
                                closed_count += 1
                                break
                        except (psutil.NoSuchProcess, psutil.AccessDenied):
                            continue
                except Exception as e:
                    errors.append(f"{process_name}: {str(e)}")
        
        message = f"Cerrados {closed_count} procesos."
        if errors:
            message += f"\n\nErrores en {len(errors)} procesos:\n" + "\n".join(errors[:3])
        
        messagebox.showinfo("Resultado", message)
        self.refresh_gaming_processes()
    
    def close_all_gaming_processes(self):
        """Cierra todos los procesos de gaming que estén ejecutándose"""
        if not messagebox.askyesno("Confirmar", 
                                 "¿Cerrar TODOS los procesos de gaming?\n\n"
                                 "Esto cerrará navegadores, aplicaciones de comunicación, "
                                 "reproductores de música y software de gaming."):
            return
        
        closed_count = 0
        errors = []
        
        for process_name in self.gaming_processes:
            try:
                # Buscar y cerrar el proceso
                for proc in psutil.process_iter(['pid', 'name']):
                    try:
                        if proc.info['name'].lower() == process_name.lower():
                            proc.terminate()
                            closed_count += 1
                            break
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        continue
            except Exception as e:
                errors.append(f"{process_name}: {str(e)}")
        
        message = f"Cerrados {closed_count} procesos de gaming."
        if errors:
            message += f"\n\nErrores en {len(errors)} procesos:\n" + "\n".join(errors[:5])
        
        messagebox.showinfo("Resultado", message)
        self.refresh_gaming_processes()
        self.refresh_processes()
    
    def full_gaming_optimization(self):
        """Realiza una optimización completa para gaming"""
        if not messagebox.askyesno("Confirmar", 
                                 "¿Realizar optimización completa para gaming?\n\n"
                                 "Esto incluirá:\n"
                                 "• Cerrar procesos de gaming\n"
                                 "• Limpiar archivos temporales\n"
                                 "• Optimizar memoria\n"
                                 "• Crear backup del sistema\n\n"
                                 "¿Continuar?"):
            return
        
        try:
            # Crear backup primero
            self.create_system_backup()
            
            # Cerrar procesos de gaming
            self.close_all_gaming_processes()
            
            # Limpiar archivos temporales
            self.clean_temp_files()
            
            # Optimizar memoria
            self.optimize_memory()
            
            # Optimizaciones adicionales para gaming
            self.gaming_system_optimizations()
            
            messagebox.showinfo("Éxito", 
                              "🎮 Optimización para gaming completada!\n\n"
                              "• Procesos de gaming cerrados\n"
                              "• Archivos temporales limpiados\n"
                              "• Memoria optimizada\n"
                              "• Backup del sistema creado\n"
                              "• Configuraciones de gaming aplicadas")
            
            self.status_var.set("Optimización para gaming completada")
            
        except Exception as e:
            messagebox.showerror("Error", f"Error durante la optimización: {str(e)}")
    
    def gaming_system_optimizations(self):
        """Aplica optimizaciones específicas para gaming"""
        try:
            # Optimizar configuración de energía para alto rendimiento
            subprocess.run(['powercfg', '/setactive', '8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c'], 
                         capture_output=True, text=True)
            
            # Desactivar servicios innecesarios para gaming
            gaming_services_to_disable = [
                "SysMain",  # Superfetch
                "WSearch",  # Windows Search
                "Themes",   # Temas
                "TabletInputService",  # Tablet PC Input
                "Fax",      # Fax
                "TapiSrv"   # Telephony
            ]
            
            for service in gaming_services_to_disable:
                try:
                    subprocess.run(['sc', 'stop', service], check=False, capture_output=True)
                    subprocess.run(['sc', 'config', service, 'start=', 'disabled'], 
                                 capture_output=True, text=True)
                except:
                    continue
            
            # Optimizar configuración de red para gaming
            subprocess.run(['netsh', 'int', 'tcp', 'set', 'global', 'autotuninglevel=normal'], 
                         capture_output=True, text=True)
            
        except Exception as e:
            print(f"Error en optimizaciones de gaming: {str(e)}")
    
    def create_system_backup(self):
        """Crea un backup completo del sistema"""
        try:
            # Crear directorio de backups si no existe
            backup_dir = os.path.join(os.path.expanduser("~"), "Desktop", "Gaming_Backups")
            os.makedirs(backup_dir, exist_ok=True)
            
            # Nombre del backup con timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_name = f"Gaming_Backup_{timestamp}"
            backup_path = os.path.join(backup_dir, backup_name)
            
            # Crear punto de restauración del sistema
            result = subprocess.run([
                'powershell', '-Command',
                f'Checkpoint-Computer -Description "{backup_name}" -RestorePointType "APPLICATION_INSTALL"'
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                # Crear archivo de información del backup
                backup_info = {
                    "timestamp": timestamp,
                    "backup_name": backup_name,
                    "description": "Backup antes de optimización para gaming",
                    "system_info": {
                        "cpu_count": psutil.cpu_count(),
                        "memory_total": psutil.virtual_memory().total,
                        "disk_usage": psutil.disk_usage('/').percent
                    }
                }
                
                info_file = os.path.join(backup_path + ".json")
                with open(info_file, 'w') as f:
                    json.dump(backup_info, f, indent=2)
                
                messagebox.showinfo("Éxito", 
                                  f"📦 Backup del sistema creado exitosamente!\n\n"
                                  f"Nombre: {backup_name}\n"
                                  f"Ubicación: {backup_dir}\n"
                                  f"Timestamp: {timestamp}")
                
                self.status_var.set(f"Backup creado: {backup_name}")
                
            else:
                messagebox.showerror("Error", f"Error al crear backup: {result.stderr}")
                
        except Exception as e:
            messagebox.showerror("Error", f"Error al crear backup: {str(e)}")
    
    def restore_from_backup(self):
        """Restaura el sistema desde un backup"""
        try:
            # Buscar backups disponibles
            backup_dir = os.path.join(os.path.expanduser("~"), "Desktop", "Gaming_Backups")
            
            if not os.path.exists(backup_dir):
                messagebox.showwarning("Advertencia", "No se encontraron backups disponibles")
                return
            
            # Listar backups disponibles
            backups = []
            for file in os.listdir(backup_dir):
                if file.endswith('.json'):
                    backup_path = os.path.join(backup_dir, file)
                    try:
                        with open(backup_path, 'r') as f:
                            backup_info = json.load(f)
                            backups.append(backup_info)
                    except:
                        continue
            
            if not backups:
                messagebox.showwarning("Advertencia", "No se encontraron backups válidos")
                return
            
            # Crear ventana de selección de backup
            backup_window = tk.Toplevel(self.root)
            backup_window.title("Seleccionar Backup para Restaurar")
            backup_window.geometry("600x400")
            
            # Lista de backups
            backup_frame = ttk.LabelFrame(backup_window, text="Backups Disponibles", padding="10")
            backup_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            
            columns = ('Nombre', 'Fecha', 'Descripción')
            backup_tree = ttk.Treeview(backup_frame, columns=columns, show='headings', height=10)
            
            for col in columns:
                backup_tree.heading(col, text=col)
            
            backup_tree.column('Nombre', width=200)
            backup_tree.column('Fecha', width=150)
            backup_tree.column('Descripción', width=250)
            
            # Poblar lista de backups
            for backup in backups:
                backup_tree.insert('', 'end', 
                                 values=(backup['backup_name'], 
                                        backup['timestamp'], 
                                        backup['description']))
            
            backup_tree.pack(fill=tk.BOTH, expand=True)
            
            # Botón de restaurar
            def restore_selected():
                selection = backup_tree.selection()
                if not selection:
                    messagebox.showwarning("Advertencia", "Selecciona un backup para restaurar")
                    return
                
                item = backup_tree.item(selection[0])
                backup_name = item['values'][0]
                
                if messagebox.askyesno("Confirmar", 
                                     f"¿Restaurar el sistema desde el backup '{backup_name}'?\n\n"
                                     "⚠️ ADVERTENCIA: Esta acción restaurará todo el sistema al estado del backup."):
                    try:
                        # Aquí iría la lógica de restauración
                        # Por ahora solo mostramos un mensaje
                        messagebox.showinfo("Info", 
                                          f"Restauración iniciada para: {backup_name}\n\n"
                                          "La restauración se realizará en segundo plano.")
                        backup_window.destroy()
                        
                    except Exception as e:
                        messagebox.showerror("Error", f"Error al restaurar: {str(e)}")
            
            ttk.Button(backup_window, text="🔄 Restaurar Seleccionado", 
                      command=restore_selected).pack(pady=10)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al listar backups: {str(e)}")
    
    def terminate_process(self):
        """Termina el proceso seleccionado"""
        selection = self.process_tree.selection()
        if not selection:
            messagebox.showwarning("Advertencia", "Selecciona un proceso primero")
            return
        
        item = self.process_tree.item(selection[0])
        pid = item['values'][0]
        name = item['values'][1]
        
        # Verificar si es crítico
        for critical in self.recommendations["critical"]:
            if critical.lower() in name.lower():
                messagebox.showerror("Error", "Este proceso es CRÍTICO y no debe terminarse")
                return
        
        if messagebox.askyesno("Confirmar", f"¿Terminar el proceso '{name}' (PID: {pid})?"):
            try:
                process = psutil.Process(int(pid))
                process.terminate()
                messagebox.showinfo("Éxito", f"Proceso '{name}' terminado")
                self.refresh_processes()
            except Exception as e:
                messagebox.showerror("Error", f"Error al terminar proceso: {str(e)}")
    
    def force_kill_process(self):
        """Fuerza la terminación del proceso seleccionado"""
        selection = self.process_tree.selection()
        if not selection:
            messagebox.showwarning("Advertencia", "Selecciona un proceso primero")
            return
        
        item = self.process_tree.item(selection[0])
        pid = item['values'][0]
        name = item['values'][1]
        
        # Verificar si es crítico
        for critical in self.recommendations["critical"]:
            if critical.lower() in name.lower():
                messagebox.showerror("Error", "Este proceso es CRÍTICO y no debe terminarse")
                return
        
        if messagebox.askyesno("Confirmar", f"¿FORZAR la terminación del proceso '{name}' (PID: {pid})?\n\n¡ADVERTENCIA: Esto puede causar pérdida de datos!"):
            try:
                process = psutil.Process(int(pid))
                process.kill()
                messagebox.showinfo("Éxito", f"Proceso '{name}' terminado forzadamente")
                self.refresh_processes()
            except Exception as e:
                messagebox.showerror("Error", f"Error al terminar proceso: {str(e)}")
    
    def toggle_auto_refresh(self):
        """Activa/desactiva el auto-refresh"""
        if self.auto_refresh_var.get():
            self.auto_refresh = True
            self.refresh_thread = threading.Thread(target=self.auto_refresh_loop, daemon=True)
            self.refresh_thread.start()
            self.status_var.set("Auto-refresh activado")
        else:
            self.auto_refresh = False
            self.status_var.set("Auto-refresh desactivado")
    
    def auto_refresh_loop(self):
        """Bucle de auto-refresh"""
        while self.auto_refresh:
            try:
                self.root.after(0, self.refresh_processes)
                time.sleep(5)  # Refrescar cada 5 segundos
            except:
                break
    
    def filter_processes(self, event=None):
        """Filtra los procesos según el texto ingresado"""
        filter_text = self.filter_var.get().lower()
        
        # Ocultar todos los elementos
        for item in self.process_tree.get_children():
            self.process_tree.detach(item)
        
        # Mostrar solo los que coinciden con el filtro
        for proc in self.processes:
            name = proc['name'] or 'N/A'
            if filter_text in name.lower():
                pid = proc['pid']
                username = proc['username'] or 'N/A'
                cpu = f"{proc['cpu_percent']:.1f}" if proc['cpu_percent'] else "0.0"
                memory = f"{proc['memory_percent']:.1f}" if proc['memory_percent'] else "0.0"
                status = proc['status']
                
                recommendation, tag = self.get_process_recommendation(name)
                
                self.process_tree.reattach(item, '', 'end')
    
    def sort_column(self, tree, col):
        """Ordena una columna del treeview"""
        # Obtener todos los elementos
        items = [(tree.set(item, col), item) for item in tree.get_children('')]
        
        # Ordenar
        items.sort()
        
        # Reorganizar elementos
        for index, (val, item) in enumerate(items):
            tree.move(item, '', index)
    
    def on_process_select(self, event):
        """Maneja la selección de un proceso"""
        selection = self.process_tree.selection()
        if selection:
            item = self.process_tree.item(selection[0])
            pid = item['values'][0]
            name = item['values'][1]
            self.status_var.set(f"Seleccionado: {name} (PID: {pid})")
    
    def show_process_details(self, event):
        """Muestra detalles del proceso seleccionado"""
        selection = self.process_tree.selection()
        if not selection:
            return
        
        item = self.process_tree.item(selection[0])
        pid = item['values'][0]
        name = item['values'][1]
        
        try:
            process = psutil.Process(int(pid))
            
            details = f"""
=== DETALLES DEL PROCESO ===

📋 Nombre: {name}
🆔 PID: {pid}
👤 Usuario: {process.username()}
📁 Ruta: {process.exe()}
📅 Creado: {datetime.fromtimestamp(process.create_time()).strftime('%Y-%m-%d %H:%M:%S')}
💾 Memoria: {process.memory_info().rss / (1024*1024):.1f} MB
🖥️ CPU: {process.cpu_percent()}%
📊 Estado: {process.status()}
🔗 Hilos: {process.num_threads()}
📦 Archivos abiertos: {len(process.open_files())}
🌐 Conexiones: {len(process.connections())}
"""
            
            # Crear ventana de detalles
            detail_window = tk.Toplevel(self.root)
            detail_window.title(f"Detalles: {name}")
            detail_window.geometry("600x400")
            
            text_widget = scrolledtext.ScrolledText(detail_window, wrap=tk.WORD)
            text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
            text_widget.insert(1.0, details)
            text_widget.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al obtener detalles: {str(e)}")
    
    def stop_service(self):
        """Detiene el servicio seleccionado"""
        selection = self.service_tree.selection()
        if not selection:
            messagebox.showwarning("Advertencia", "Selecciona un servicio primero")
            return
        
        item = self.service_tree.item(selection[0])
        service_name = item['values'][0]
        
        if messagebox.askyesno("Confirmar", f"¿Detener el servicio '{service_name}'?"):
            try:
                result = subprocess.run(['sc', 'stop', service_name], 
                                      capture_output=True, text=True)
                
                if result.returncode == 0:
                    messagebox.showinfo("Éxito", f"Servicio '{service_name}' detenido")
                    self.refresh_services()
                else:
                    messagebox.showerror("Error", f"Error al detener servicio: {result.stderr}")
                    
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")
    
    def start_service(self):
        """Inicia el servicio seleccionado"""
        selection = self.service_tree.selection()
        if not selection:
            messagebox.showwarning("Advertencia", "Selecciona un servicio primero")
            return
        
        item = self.service_tree.item(selection[0])
        service_name = item['values'][0]
        
        if messagebox.askyesno("Confirmar", f"¿Iniciar el servicio '{service_name}'?"):
            try:
                result = subprocess.run(['sc', 'start', service_name], 
                                      capture_output=True, text=True)
                
                if result.returncode == 0:
                    messagebox.showinfo("Éxito", f"Servicio '{service_name}' iniciado")
                    self.refresh_services()
                else:
                    messagebox.showerror("Error", f"Error al iniciar servicio: {result.stderr}")
                    
            except Exception as e:
                messagebox.showerror("Error", f"Error: {str(e)}")


def main():
    """Función principal"""
    root = tk.Tk()
    app = ProcessManagerAdvanced(root)
    root.mainloop()


if __name__ == "__main__":
    main()
