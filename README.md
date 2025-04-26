Bu fonksiyon, n adet işin m adet makine üzerinde en az toplam süreyle tamamlanmasını sağlar.
Her işin her makinede farklı sürelerde tamamlandığı bir durumda, makineler arası geçişin de maaliyeti olduğu varsayılır.
Amaç, işleri bir sırayla işleyerek toplam süreyi minimize etmektir.
def min_total_time(n, m, time, cost): iççin n toplam iş, m makine sayısını, time ile istenen durumdaki tamamlanma süresi ve cost ile istenilen durumdaki geçiş maaliyeti alınır.
dp = [[float('inf')] * m for _ in range(n)] ile dinamik programlama tablosu oluşturulur.
for j in range(m):
dp[0][j] = time[0][j] ilk iş için her makinede bitirilme süresi belirlenir.
for i in range(1, n): birinci işten n-1 işine kadar döngü yapar.
for j in range(m): j anlık makineyi gösterir.
for k in range(m): k bir önceki işin işlendiği makineyi gösterir.
return min(dp[n-1]) ile her makinede oluşan toplam süreler içinden en küçüğü seçilir.
Bu problemde verilen n adet iş sırasıyla yapılmak zorundadır. Bu işler, m farklı makinede çalıştırılabilir.
Her işin her makinede farklı bir süresi vardır, ve bir işten sonra başka bir makineye geçmek ek maliyet getirir. Amaç, sırayla birer makinede çalıştırarak, toplam süreyi minimuma indirmektir.
Matris çarpımına benzerliği işlemleri belirli sırada yapması, her adımda farklı seçimlerin farklı maaliyetler doğurması, dinamik programlamayla çözülmesi ve alt probleler çözülerek toplam en düşük maaliyet hesaplanması olarak alınabilir.
Zaman karmaşıklığı 	O(n × m²), uzay karmaşıklığı  O(n × m) olarak bulunabilir.
