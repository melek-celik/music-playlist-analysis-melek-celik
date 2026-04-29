# Music Playlist Analysis System

def get_total_duration(songs):
    """Tüm şarkıların toplam süresini saniye cinsinden hesaplar."""
    total = sum(song['sure'] for song in songs)
    return total

def get_most_played_song(songs):
    """En çok dinlenen şarkıyı bulur."""
    most_played = max(songs, key=lambda x: x['dinlenme_sayisi'])
    return most_played

def get_average_duration(songs):
    """Ortalama şarkı süresini hesaplar."""
    if not songs: return 0
    return sum(song['sure'] for song in songs) / len(songs)

def get_longest_song(songs):
    """BONUS: Listenin en uzun şarkısını bulur."""
    return max(songs, key=lambda x: x['sure'])

def print_playlist(songs):
    """Çalma listesini düzenli bir tablo formatında yazdırır."""
    print("\n--- Müzik Çalma Listesi ---")
    print(f"{'Şarkı Adı':<20} | {'Sanatçı':<15} | {'Süre':<6} | {'Dinlenme'}")
    print("-" * 55)
    for song in songs:
        print(f"{song['sarki_adi']:<20} | {song['sanatci_adi']:<15} | {song['sure']:<6} | {song['dinlenme_sayisi']}")

def main():
    # En az 5 şarkı içeren liste ve sözlük yapısı
    playlist = [
        {"sarki_adi": "Starboy", "sanatci_adi": "The Weeknd", "sure": 230, "dinlenme_sayisi": 1500000},
        {"sarki_adi": "Blinding Lights", "sanatci_adi": "The Weeknd", "sure": 200, "dinlenme_sayisi": 2800000},
        {"sarki_adi": "Mockingbird", "sanatci_adi": "Eminem", "sure": 250, "dinlenme_sayisi": 1200000},
        {"sarki_adi": "Shape of You", "sanatci_adi": "Ed Sheeran", "sure": 233, "dinlenme_sayisi": 3000000},
        {"sarki_adi": "Bohemian Rhapsody", "sanatci_adi": "Queen", "sure": 354, "dinlenme_sayisi": 2100000}
    ]

    # Metodların aktif olarak çağırılması
    print_playlist(playlist)
    
    total_sec = get_total_duration(playlist)
    most_played = get_most_played_song(playlist)
    avg_dur = get_average_duration(playlist)
    longest = get_longest_song(playlist)

    # Analiz sonuçlarının ekrana yazdırılması
    print("\n--- Analiz Sonuçları ---")
    print(f"Toplam Çalma Süresi: {total_sec} saniye")
    print(f"Ortalama Şarkı Süresi: {avg_dur:.2f} saniye")
    print(f"En Çok Dinlenen: {most_played['sarki_adi']} ({most_played['dinlenme_sayisi']} dinlenme)")
    print(f"En Uzun Şarkı: {longest['sarki_adi']} ({longest['sure']} saniye)")

if __name__ == "__main__":
    main()