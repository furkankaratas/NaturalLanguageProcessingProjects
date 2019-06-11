import random
import math

#İki d boyutlu nokta arasındaki öklid uzaklığı bulacağız.
def oklikuzakligi(p0,p1):
    uzaklik=0.0
    for i in range(0,len(p0)):
        uzaklik += (p0[i]-p1[i]) ** 2
    return math.sqrt(uzaklik)

#k-means algoritması
def kmeans(k,datapoints):
    d=len(datapoints[0])

    Max_iterasyon=1000
    i=0

    kume=[0]*len(datapoints)
    onceki_kume=[-1] * len(datapoints)

    #rastgele kümeler için merkez belirleyeceğiz(seçeceğiz.)
    kume_merkezleri=[]
    for i in range(0,k):
        yeni_kume = []
        kume_merkezleri += [random.choice(datapoints)]

        force_recalculation=False
    #rastgele seçilen noktalar kötü olabilir force_recalculation false edilir.
    while (kume!= onceki_kume) or (i>Max_iterasyon) or (force_recalculation):

        onceki_kume=list(kume)
        force_recalculation=False
        i += 1

    #nokta dizisinin merkez noktasının güncellenmesi
    for p in range(0, len(datapoints)):
        enkucuk_uzaklik=float("inf")
        #Tüm merkezlerin minimum uzaklık olduğu kontrol edilir.
        for c in range(0,len(kume_merkezleri)):

            uzaklik=oklikuzakligi(datapoints[p], kume_merkezleri[c])
            #noktayı yeni kümeye atama işlemi
            if (uzaklik<enkucuk_uzaklik):
                enkucuk_uzaklik=uzaklik
                kume[p]=c
    #Kümelerin pozisyonlarının güncellenmesi
    for k in range(0, len(kume_merkezleri)):
        yeni_merkez=[0]*d
        noktalar=0
        for p in range(0,len(datapoints)):
            if(kume[p]==k):
                for j in range(0,d):
                    yeni_merkez[j] += datapoints[p][j]
                    noktalar += 1

        for j in range(0,d):
            if noktalar!=0:
                yeni_merkez[j]=yeni_merkez[j] / float(noktalar)

            #ilk seçilen nokta kötü ise; yeni bir nokta belirle.
            else:
                yeni_merkez=random.choice(datapoints)
                force_recalculation = True
                print("Zorunlu olarak yeniden hesaplanıyor.")

        kume_merkezleri[k]=yeni_merkez

    print("******     Sonuçlar   *****")
    print("Kümeler : ", kume_merkezleri)
    print("Adım sayısı : ", i)
    print("Küme : ", kume)

#main fonksiyonu
if __name__ == "__main__":
    # Veri noktaları -> n boyutlu vektörlerin listesi

    datapoints = [(3, 2), (2, 2), (1, 2), (0, 1), (1, 9), (1, 1), (5, 4), (7, 7), (9, 10), (11, 13), (12, 12), (12, 9),
                  (13, 13),(4,9),(6,10),(1,1)]

    k = 4 # küme sayısı

    kmeans(k, datapoints)
