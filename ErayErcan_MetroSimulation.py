from collections import defaultdict, deque
import heapq
from typing import Dict, List, Set, Tuple, Optional

class Istasyon:
    def __init__(self, idx: str, ad: str, hat: str):
        self.idx = idx
        self.ad = ad
        self.hat = hat
        self.komsular: List[Tuple['Istasyon', int]] = [] ## Komşu istasyonları ve bu istasyonlara ulaşım sürelerini tutan liste 

    def komsu_ekle(self, istasyon: 'Istasyon', sure: int):
        self.komsular.append((istasyon, sure))

    def __lt__(self, other: 'Istasyon'):
        return self.idx < other.idx  # İstasyonları sıralamak için
class MetroAgi:
    def __init__(self):  
        self.istasyonlar: Dict[str, Istasyon] = {}  # İstasyonları tutar
        self.hatlar: Dict[str, List[Istasyon]] = defaultdict(list)  # Hatlara ait istasyonları tutar

    def istasyon_ekle(self, idx: str, ad: str, hat: str) -> None:  
        if idx not in self.istasyonlar: 
            istasyon = Istasyon(idx, ad, hat) 
            self.istasyonlar[idx] = istasyon
            self.hatlar[hat].append(istasyon)

    def baglanti_ekle(self, istasyon1_id: str, istasyon2_id: str, sure: int) -> None: 
        istasyon1 = self.istasyonlar[istasyon1_id]
        istasyon2 = self.istasyonlar[istasyon2_id]
        istasyon1.komsu_ekle(istasyon2, sure)
        istasyon2.komsu_ekle(istasyon1, sure)
    
    def en_az_aktarma_bul(self, baslangic_id: str, hedef_id: str) -> Optional[List[Istasyon]]:
        
        # BFS ile en az aktarmalı rota bulma
        
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:
            return None
        
        baslangic = self.istasyonlar[baslangic_id] # Başlangıç istasyon
        hedef = self.istasyonlar[hedef_id] # Hedef istasyon
        kuyruk = deque([(baslangic, [baslangic])]) # Kuyruk veri yapısı, başlangıç düğümü ile başlatılır
        ziyaret_edildi = {baslangic.idx} # Ziyaret edilen düğümleri tutar
        
        while kuyruk: 
            mevcut, yol = kuyruk.popleft()  # Kuyruktan bir düğüm çıkar
            if mevcut == hedef:
                return yol
            
            for komsu, _ in mevcut.komsular:      # Komsuları gez
                if komsu not in ziyaret_edildi: 
                    ziyaret_edildi.add(komsu)
                    kuyruk.append((komsu, yol + [komsu]))  
        
        return None
        
    def en_hizli_rota_bul(self, baslangic_id: str, hedef_id: str) -> Optional[Tuple[List[Istasyon], int]]: 
        # A* ile en hızlı rota bulma
        
        if baslangic_id not in self.istasyonlar or hedef_id not in self.istasyonlar:   # İstasyonlar mevcut mu kontrolü
            return None
        
        baslangic = self.istasyonlar[baslangic_id] 
        hedef = self.istasyonlar[hedef_id]
        
        oncelikli_kuyruk = [(0, baslangic, [baslangic])]  # Öncelikli kuyruk oluştur (ilk eleman: (toplam süre, başlangıç istasyonu, izlenen yol))
        en_iyi_sure = {baslangic.idx: 0}  # En iyi süreleri tutar
        
        while oncelikli_kuyruk:
            veri = heapq.heappop(oncelikli_kuyruk)  
            if len(veri) == 4:   # Veri uzunluğu kontrolü
                mevcut_sure, _, mevcut, yol = veri
            else:
                mevcut_sure, mevcut, yol = veri

            
            if mevcut == hedef:
                return yol, mevcut_sure
            
            for komsu, sure in mevcut.komsular: 
                yeni_sure = mevcut_sure + sure
                
                if komsu.idx not in en_iyi_sure or yeni_sure < en_iyi_sure[komsu.idx]:  # Eğer istasyon daha önce ziyaret edilmediyse veya daha kısa bir yol bulunduysa
                    en_iyi_sure[komsu.idx] = yeni_sure    # Yeni En iyi süreyi güncelle
                    heapq.heappush(oncelikli_kuyruk, (yeni_sure, id(komsu),komsu, yol + [komsu]))
                    
        return None
        

# Örnek Kullanım
if __name__ == "__main__":
    metro = MetroAgi()
    
    # İstasyonlar ekleme
    # Kırmızı Hat
    metro.istasyon_ekle("K1", "Kızılay", "Kırmızı Hat")
    metro.istasyon_ekle("K2", "Ulus", "Kırmızı Hat")
    metro.istasyon_ekle("K3", "Demetevler", "Kırmızı Hat")
    metro.istasyon_ekle("K4", "OSB", "Kırmızı Hat")
    
    # Mavi Hat
    metro.istasyon_ekle("M1", "AŞTİ", "Mavi Hat")
    metro.istasyon_ekle("M2", "Kızılay", "Mavi Hat")  # Aktarma noktası
    metro.istasyon_ekle("M3", "Sıhhiye", "Mavi Hat")
    metro.istasyon_ekle("M4", "Gar", "Mavi Hat")
    
    # Turuncu Hat
    metro.istasyon_ekle("T1", "Batıkent", "Turuncu Hat")
    metro.istasyon_ekle("T2", "Demetevler", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T3", "Gar", "Turuncu Hat")  # Aktarma noktası
    metro.istasyon_ekle("T4", "Keçiören", "Turuncu Hat")
    
    # Bağlantılar ekleme
    # Kırmızı Hat bağlantıları
    metro.baglanti_ekle("K1", "K2", 4)  # Kızılay -> Ulus
    metro.baglanti_ekle("K2", "K3", 6)  # Ulus -> Demetevler
    metro.baglanti_ekle("K3", "K4", 8)  # Demetevler -> OSB
    
    # Mavi Hat bağlantıları
    metro.baglanti_ekle("M1", "M2", 5)  # AŞTİ -> Kızılay
    metro.baglanti_ekle("M2", "M3", 3)  # Kızılay -> Sıhhiye
    metro.baglanti_ekle("M3", "M4", 4)  # Sıhhiye -> Gar
    
    # Turuncu Hat bağlantıları
    metro.baglanti_ekle("T1", "T2", 7)  # Batıkent -> Demetevler
    metro.baglanti_ekle("T2", "T3", 9)  # Demetevler -> Gar
    metro.baglanti_ekle("T3", "T4", 5)  # Gar -> Keçiören
    
    # Hat aktarma bağlantıları (aynı istasyon farklı hatlar)
    metro.baglanti_ekle("K1", "M2", 2)  # Kızılay aktarma
    metro.baglanti_ekle("K3", "T2", 3)  # Demetevler aktarma
    metro.baglanti_ekle("M4", "T3", 2)  # Gar aktarma
    
    # Test senaryoları
    print("\n=== Test Senaryoları ===")
    
    # Senaryo 1: AŞTİ'den OSB'ye
    print("\n1. AŞTİ'den OSB'ye:")
    rota = metro.en_az_aktarma_bul("M1", "K4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("M1", "K4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 2: Batıkent'ten Keçiören'e
    print("\n2. Batıkent'ten Keçiören'e:")
    rota = metro.en_az_aktarma_bul("T1", "T4")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T1", "T4")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota))
    
    # Senaryo 3: Keçiören'den AŞTİ'ye
    print("\n3. Keçiören'den AŞTİ'ye:")
    rota = metro.en_az_aktarma_bul("T4", "M1")
    if rota:
        print("En az aktarmalı rota:", " -> ".join(i.ad for i in rota))
    
    sonuc = metro.en_hizli_rota_bul("T4", "M1")
    if sonuc:
        rota, sure = sonuc
        print(f"En hızlı rota ({sure} dakika):", " -> ".join(i.ad for i in rota)) 