# Import library yang diperlukan
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk simulasi
def simulate_rumor_spread(t_max, dt=0.1, 
                         total_population=10000,
                         initial_spreaders=100,
                         spread_rate=0.3,
                         skepticism_rate=0.1,
                         verification_rate=0.05):
    # Inisialisasi parameter
    N = total_population
    I0 = initial_spreaders
    S0 = N - I0
    R0 = 0
    α = spread_rate
    β = skepticism_rate
    γ = verification_rate
    
    # Inisialisasi array waktu
    t = np.arange(0, t_max, dt)
    
    # Inisialisasi array untuk menyimpan hasil
    S = np.zeros(len(t))  # Susceptible
    I = np.zeros(len(t))  # Infected (penyebar rumor)
    R = np.zeros(len(t))  # Recovered
    
    # Kondisi awal
    S[0] = S0
    I[0] = I0
    R[0] = R0
    
    # Simulasi menggunakan model SIR yang dimodifikasi
    for i in range(1, len(t)):
        # Perubahan populasi berdasarkan interaksi
        dS = (-α * S[i-1] * I[i-1] / N) * dt
        dI = (α * S[i-1] * I[i-1] / N - β * I[i-1] - γ * I[i-1]) * dt
        dR = (β * I[i-1] + γ * I[i-1]) * dt
        
        # Update populasi
        S[i] = S[i-1] + dS
        I[i] = I[i-1] + dI
        R[i] = R[i-1] + dR
    
    return t, S, I, R

# Fungsi untuk plotting
def plot_results(t, S, I, R, params):
    plt.figure(figsize=(12, 6))
    
    # Plot ketiga kurva
    plt.plot(t, S, 'b-', label='Belum terpapar rumor', linewidth=2)
    plt.plot(t, I, 'r-', label='Penyebar rumor aktif', linewidth=2)
    plt.plot(t, R, 'g-', label='Sadar rumor itu salah', linewidth=2)
    
    # Mempercantik plot
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.title('Simulasi Penyebaran Rumor di Media Sosial', pad=15, fontsize=14)
    plt.xlabel('Waktu (hari)', fontsize=12)
    plt.ylabel('Jumlah Pengguna', fontsize=12)
    plt.legend(fontsize=10)
    
    # Menambahkan informasi parameter
    info_text = f'Parameter:\nPopulasi Total = {params["total_population"]:,}\n'
    info_text += f'Penyebar Awal = {params["initial_spreaders"]}\n'
    info_text += f'Tingkat Penyebaran (α) = {params["spread_rate"]}\n'
    info_text += f'Tingkat Skeptisisme (β) = {params["skepticism_rate"]}\n'
    info_text += f'Tingkat Verifikasi (γ) = {params["verification_rate"]}'
    
    plt.text(0.02, 0.98, info_text,
            transform=plt.gca().transAxes,
            verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    plt.show()

# Parameter simulasi
params = {
    'total_population': 10000,    # Total pengguna media sosial
    'initial_spreaders': 100,     # Jumlah awal penyebar rumor
    'spread_rate': 0.3,          # Tingkat penyebaran rumor
    'skepticism_rate': 0.1,      # Tingkat skeptisisme
    'verification_rate': 0.05     # Tingkat verifikasi
}

# Menjalankan simulasi
t, S, I, R = simulate_rumor_spread(
    t_max=30,  # Simulasi selama 30 hari
    **params   # Unpack parameter simulasi
)

# Visualisasi hasil
plot_results(t, S, I, R, params)