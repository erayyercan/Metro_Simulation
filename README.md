# Metro Simulation
----
## 1. Proje Başlığı ve Kısa Açıklama

Metro Simulation, bir metro ağında en az aktarma ve en hızlı rota bulmayı sağlayan bir Python uygulamasıdır. Kullanıcılar, belirli başlangıç ve hedef istasyonlarını seçerek metro ağındaki en optimal rotayı bulabilirler.
---

## 2. Kullanılan Teknolojiler ve Kütüphaneler

Projede aşağıdaki Python kütüphaneleri kullanılmıştır:

- **collections:** `defaultdict` ve `deque` veri yapıları ile verimli veri yönetimi sağlamak için kullanılmıştır.

- **heapq:** Öncelikli kuyruğu yönetmek ve en kısa sürede ulaşılacak rotayı hesaplamak için kullanılmıştır.

- **typing:** Tip ipuçları ekleyerek kodun okunabilirliğini artırmak için kullanılmıştır.
---

  ## 3. Algoritmaların Çalışma Mantığı
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

  
