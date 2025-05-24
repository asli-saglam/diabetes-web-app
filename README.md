# Diyabet Tahmin Uygulaması

Bu repo, Global AI Hub Bootcamp kapsamında gerçekleştirdiğim Diyabet Tahmin Projesi'ni içermektedir. Projede hem gözetimli hem de gözetimsiz öğrenme algoritmaları uygulanmış, aynı zamanda Streamlit ile web arayüzü oluşturularak model deploy edilmiştir. Ayrıca GPU destekli model eğitimi gerçekleştirilerek performans karşılaştırması yapılmıştır.

 # Giriş

Projede, CDC'nin BRFSS 2015 veri seti kullanılarak bireylerin diyabet hastalığı riskini tahmin etmeye yönelik bir makine öğrenmesi sistemi geliştirilmiştir. Veri seti "balanced" olacak şekilde 0 ve 1 sınıfları dengelenmiştir.

# Proje kapsamında uygulanan temel adımlar:

- Keşifsel Veri Analizi (EDA)

- Veri Ön işleme (eksik değer, normalizasyon, vs.)

- Modelleme (Logistic Regression, KNN, SVM, Random Forest)

- Karşılaştırmalı metrik değerlendirme

- Hiperparametre optimizasyonu (SVM için)

- Web arayüzü ile son kullanıcı etkileşimi (Streamlit)

- GPU destekli model eğitimi (RAPIDS - cuML)


# Kullanılan Algoritmalar ve Seçim Gerekçeleri

Dört farklı makine öğrenmesi algoritması uygulanmıştır:

Logistic Regression -> Hızlı ve yorumlanabilir bir baz model

K-Nearest Neighbors -> Basit ve örnek temelli modelleme

SVM                 -> Küçük/orta boyutlu veri setlerinde başarılı, karar sınırı iyi

Random Forest       -> Ensemble yapısıyla aşırı öğrenmeye dayanıklı

Yapılan karşılaştırmada en yüksek F1 skoru 0.762952 değeri ile SVM modeli olduğu için bu modelin hiperparametre optimizasyonu yapılmış ve kullanılacak model olarak seçilmiştir.

# Model Performansı

En iyi model olan SVM (RBF kernel ile, C=10, gamma=0.01) değerleri ile değerlendirilmiştir:


Accuracy  -> 0.78

Precision -> 0.76

Recall    -> 0.80

F1 Score  -> 0.78

Confusion Matrix görselleştirmesi ile tahmin başarısı detaylandırılmıştır:

![image](https://github.com/user-attachments/assets/004a7037-5e33-4742-9601-40d861a1410c)


# BONUS 1: Gözetimsiz Öğrenme – KMeans Kümeleme

Veri setinde diyabetli ve diyabetsiz bireylerin ortak özelliklerini belirlemek için KMeans algoritması ile kümeleme yapılmıştır.

- Elbow Yöntemi kullanılarak en uygun küme sayısı = 2 bulundu.

- PCA ile boyut indirgeme yapılarak kümeler görselleştirildi.

- Küme içindeki bireylerin ortalama değerlerine bakılarak sağlık profilleri analiz edildi.

Bu analiz, diyabet riski yüksek bireylerin toplu özelliklerini anlamamıza yardımcı oldu.

# BONUS 2: GPU Destekli Model Eğitimi (cuML)

cuml.svm.SVC ile RAPIDS ekosistemi kullanılarak GPU ortamında model eğitildi. CPU ile eğitilen SVM ile performans karşılaştırması aşağıdaki gibidir:

Kriter               CPU (sklearn)              GPU (cuML)
Eğitim Süresi        14dk                         2dk

Accuracy             0.78                         0.78
F1 Score             0.78                         0.78

Sonuç: Eğitim süresi ciddi şekilde azaldı, özellikle büyük veri setleri için GPU büyük avantaj sunmaktadır.

# BONUS 3: Web Arayüzü ile Kullanıcı Etkileşimi

Projeye, son kullanıcıların model ile etkileşime geçebileceği bir Streamlit arayüzü eklendi.

Kullanıcıdan yaş, kilo, boy, sigara/alkol kullanımı gibi bilgiler alınıyor.

BMI değeri kullancılara kolaylık sağlamak açısından sistem tarafından hesaplanıyor.

Girilen veriler model tarafından tahmin edilerek diyabet riski veriliyor.

Web Arayüzü:
![image](https://github.com/user-attachments/assets/43378f07-ad9a-4ce5-b69a-3eedcf766835)



# Sonuç ve Gelecek Çalışmalar

Bu proje, temel gözetimli ve gözetimsiz öğrenme yöntemlerini başarıyla uygulayarak diyabet tahmini üzerine etkili bir çözüm sunmuştur. Gelecekte, daha geniş ve çeşitli veri setleri kullanılarak (örneğin farklı yıllara ait BRFSS veya NHANES verileri) modelin genellenebilirliği artırılabilir. Ayrıca yapay sinir ağları (ANN) veya evrişimli sinir ağları (CNN) gibi derin öğrenme teknikleriyle model performansı daha da iyileştirilebilir. Gerçek zamanlı veri toplama yeteneği (örneğin bir mobil uygulama entegrasyonu) sayesinde kullanıcı etkileşimi artırılabilir. Son olarak, kullanıcıların kişisel sağlık profillerine özel öneriler sunan karar destek sistemleri geliştirilerek projenin pratik sağlık hizmetlerine entegrasyonu sağlanabilir.

# Linkler
Gözetimli Öğrenme  -> https://www.kaggle.com/code/aslisaglam/supervised

Gözetimsiz Öğrenme -> https://www.kaggle.com/code/aslisaglam/unsupervised

Web Arayüzü        -> https://www.kaggle.com/code/aslisaglam/diabets-project

# Teşekkür

Bu proje, Global AI Hub Bootcamp'inde edindiğim bilgiler ve desteklerle gerçekleşmiştir. Emeği geçen tüm mentörlere teşekkür ederim.

