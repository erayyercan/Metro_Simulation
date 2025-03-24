# Metro Simulation
----

## 1. Kullanılan Teknolojiler ve Kütüphaneler

Projede aşağıdaki Python kütüphaneleri kullanılmıştır:

- **collections:** `defaultdict` ve `deque` veri yapıları ile verimli veri yönetimi sağlamak için kullanılmıştır.

- **heapq:** Öncelikli kuyruğu yönetmek ve en kısa sürede ulaşılacak rotayı hesaplamak için kullanılmıştır.

- **typing:** Tip ipuçları ekleyerek kodun okunabilirliğini artırmak için kullanılmıştır.
---

  ## 2. Algoritmaların Çalışma Mantığı
Projede iki farklı rota bulma algoritması kullanılmıştır:

### BFS (Genişlik Öncelikli Arama) Algoritması
Bu algoritma, en az aktarma gerektiren rotayı bulmak için kullanılmıştır. BFS, bir grafikte belirli bir başlangıç noktasından tüm düğümleri katman katman ziyaret ederek en kısa aktarma sayısını bulan bir algoritmadır.
- Başlangıç istasyonundan itibaren komşu istasyonlar bir kuyruğa eklenir.

- Ziyaret edilen istasyonlar kaydedilir ve tekrar ziyaret edilmez.

- Hedef istasyona ulaşıldığında algoritma durur ve en kısa aktarma rotasını döndürür.

### A (A Star) Algoritması*

Bu algoritma, en hızlı rotayı bulmak için kullanılmıştır. BFS gibi düğümleri genişlik öncelikli ziyaret eder ancak her adımda toplam seyahat süresini dikkate alarak en iyi tahmini süreye sahip düğümü önceliklendirir.
- Öncelikli bir kuyruk `heapq` kullanılarak, en düşük toplam süresi olan rota seçilir.

- İstasyonlar ve bağlantılar arasındaki süreler hesaplanarak en hızlı güzergah belirlenir.

- Hedef istasyona ulaşıldığında algoritma durur ve en kısa sürede varılacak rotayı döndürür.
  
### Neden Bu Algoritmalar Kullanıldı?

- **BFS**, en kısa yol yerine en az aktarmalı rotayı bulmada oldukça etkilidir.

- **A algoritması***, en kısa sürede hedefe ulaşmayı sağladığı için daha doğru ve hızlı sonuçlar üretir.
---

## 3.Örnek Kullanım ve Test Sonuçları

Metro ağı aşağıdaki istasyonları ve hatları içermektedir:

### Kırmızı Hat

- **Kızılay (K1)**

- **Ulus (K2)**

- **Demetevler (K3)**

- **OSB (K4)**

### Mavi Hat

- **AŞTİ (M1)**

- **Kızılay (M2)** (Aktarma İstasyonu)

- **Sıhhiye (M3)**

- **Gar (M4)**

### Turuncu Hat

- **Batıkent (T1)**

- **Demetevler (T2)** (Aktarma İstasyonu)

- **Gar (T3)** (Aktarma İstasyonu)

- **Keçiören (T4)**
---

### Test Senaryoları

1. `AŞTİ (M1)` -> `OSB (K4)`


2. `Batıkent (T1)` -> `Keçiören (T4)`


3. `Keçiören (T4)` -> `AŞTİ (M1)`
---

### Test Sonuçları

Verilen test seneryoları uygulandığında BFS ve A* algoritmaları sonuçları bu şekilde:



  
