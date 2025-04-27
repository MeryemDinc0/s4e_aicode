# s4e_aicode
Bu proje, kullanıcıların sağladığı metin tabanlı açıklamalar üzerinden Python kodu üreten bir web uygulaması oluşturmak için Flask kullanarak geliştirilmiştir. Uygulama, Ollama modelini Docker üzerinden çalıştırarak, kullanıcının girdiği prompt'a göre kod üretir.

Gerekli Uygulamalar/Modeller
1)Ollama
2)Minikube
3)Docker
4)Kubernetes
5) Helm chart


Uygulamarın Kurulumu
1)Ollama
"brew install ollama" ile MAC terminalinde ollamayı kurdum. "lsof -i :11434" ile portu kimin kullandığına baktım ve sonucunda "ollama is running" çıktısını aldım. 


2)Minikube
Minikube'yi kurdum. MAC terminalinde minikubeyi başlattım. "minikube start" 
Daha sonra "minikube tunnel" ile yerel ağ üzerinde Kubernetes servisini kullanabildim.

3)Docker
Resmi sitesinden indirip kurdum. 
"docker run -d --name ollama -p 11434:11434 ollama/ollama" kodunu visual studio terminalinde çalıştırım. Yani Ollama modelini Docker container'ında başlatmasını sağladım."docker ps" ile ollamanın ID, kullandığı portu her şeyi görebildim. 

4)Kubernetes
Kubernetes, uygulama bileşenlerini konteynerlerde çalıştırmayı ve yönetmeyi kolaylaştıran bir platformdur. Bu projede "ollama-deployment.yaml , ollama-service.yaml , web-deployment.yaml , web-service.yaml" dosyalarını kullanmamın amacı, Ollama modelinin Kubernetes ortamında çalışabilmesi için gerekli yapılandırmayı sağlamaktır.Bu dosya, Ollama servisini Kubernetes üzerinde başlatmak ve dağıtmak için gerekli adımları tanımlar.

5)Helm chart
Helm Chart, Kubernetes uygulamaları için şablonlar ve yapılandırmalar içeren bir pakettir. Bu şablonlar, Kubernetes kaynaklarını (Deployment, Service, ConfigMap, Secret, vb.) oluştururken, parametrelerin kolayca yapılandırılmasına imkan verir. Helm kullanarak bu şablonları daha dinamik hale getirebiliriz.


Kodun Yapısı
1)requirements.tsxt
"requirements.txt" dosyasında Flask ,openai, ollama, requests gibi gereklilikleri yazdım. 

2)app.py
Flask web uygulamasının ana dosyasıdır. Kullanıcıdan prompt alıyor, modeli çağırıyor ve üretilen kodu kullanıcıya sunuyor.

3)your_model.py
Ollama modeline bağlanıyor ve verilen prompt'a göre Python kodu üretiyor. generate_code fonksiyonu bu işlemi gerçekleştirir.

4)templates/index.html
Kullanıcı arayüzü (frontend) kısmıdır. Kullanıcı buraya prompt yazar ve çıktıyı görür.

5)ollama-deployment.yaml ve web-deployment.yaml
Deployment kısmı, Kubernetes'e hangi container'ların ne kadar sayıda çalıştırılacağını, bu container'lar için gerekli kaynakları (CPU, bellek vb.) ve bu container'ların nasıl çalıştırılacağını belirtir. Dolayısıyla Ollama modelini Docker konteynerında çalıştırıyoruz ve Kubernetes, bu konteyneri bir pod içinde çalıştıracak.

6)ollama-service.yaml ve web-service.yaml
Service kısmı, dış dünyadan gelen taleplerin Kubernetes cluster'ında hangi pod'lara yönlendirileceğini belirtir.Eğer Ollama modeline bir istek göndermek istiyorsak, bu istek Kubernetes servisleri aracılığıyla doğru pod'a yönlendirilir.

7)Helm Chart yapısı
Helm Chart kullanarak, projemi aşağıdaki adımlarla Kubernetes ortamına dağıttım.
Helm Chart, genellikle bir proje dizininde yer alan bir dizi YAML şablonunu içerir.Benim YAML şablonlarım şunlar:
   deployment.yaml: Kubernetes pod'larının nasıl çalışacağını tanımlar.
   service.yaml: Uygulamaya dışarıdan nasıl erişileceğini belirler.
   values.yaml: Değişkenler ve parametrelerin yapılandırılabileceği dosya.

Helm Chart'ı projeme entegre etmek için içeriklerini istediğim gibi şekillendirdim.
Helm Chart’ı uygulamaya uygulamak için şu adımları gerçekleştirdim:
   "helm install my-ollama ./path/to/chart" (Chart'ı yüklemek için)
   "helm status my-ollama" (Helm Chart ile dağıtımın durumunu görmek için)

Helm Chart sayesinde, Kubernetes ortamına Ollama modelinin konteynerini ve servisini kolayca dağıttım. "helm install" komutuyla Helm, bu şablonları alıp Kubernetes kaynaklarını oluşturdu.



Uygulamanın Çalışması
1)Flask uygulamasını başlatma
"python3 /Users/meryemdinc/Documents/s4e_devops/ai-code-generator/app.py" kodu ile http://127.0.0.1:5001 adresine ulaşabildim. 

2)Ollama'nın Docker ile çalışması
"docker run -d --name ollama -p 11434:11434 ollama/ollama" 
Böylece bu komut, Ollama modelini 11434 portunda çalıştıracaktır.

3) Tünel açma
Mac terminalinde "minikube start" ile minukubeyi başlattım ve "minikube tunnel" ile tünelimi açtım.

Sonuç olarak "http://127.0.0.1:5001" adresine girince sayfam açılıyor ve promptumu girince hem sayfadan hem de terminalden çıktımı alıyorum. Ek olarak çıktıları ve görüntüleri de aşağı bırakacağım. 



[ai-code-cıktısı.pdf](https://github.com/user-attachments/files/19930273/ai-code-ciktisi.pdf)
