# Readme
**Autor : Richard Dubny**
**Projekt : Anomaly Detection in Python**
**Rok: 2023**

## Detekce Anomálií s Isolation Forest

Tento skript implementuje detekci anomálií pomocí algoritmu Isolation Forest.
Tento algoritmus je součástí knihovny `sklearn.ensemble` v Pythonu, která je součástí balíčku scikit-learn.

## Instalace

Před spuštěním skriptu si ujistěte, že máte nainstalované potřebné závislosti. 
Můžete je nainstalovat pomocí následujících příkazů:

`pip install pandas`&&`pip install scikit-learn`
 
## Použití
Stáhněte tento repozitář na své lokální zařízení pomocí příkazu :
`git clone https://github.com/username/AnomalyDetection-IsolationForest`

Ve svém terminálu přejděte do adresáře, kde je tento skript umístěn.

Spusťte skript následujícím způsobem:

`python script.py <file_path>`

** poznamka: <file_path> je cesta k CSV souboru obsahujícímu bezpečnostní data.

## Struktura kódu
**script.py**: Hlavní skript pro detekci anomálií.
**utils.py**: Obsahuje funkce pro načtení dat a předzpracování, které jsou použity v script.py.
**anomaly_detection.py**: Obsahuje funkci pro detekci anomálií s použitím algoritmu Isolation Forest.

<strong>Zmen jmena promenych pls toto je hruza</strong>

## 'load_data(file_path)'
Tato funkce načte data ze zadaného CSV souboru a vrátí je ve formátu DataFrame.

## 'preprocess_data(data)'
Tato funkce provádí předzpracování dat. 

## 'detect_anomalies(data)'
Tato funkce provádí detekci anomálií pomocí algoritmu Isolation Forest. 

## Výstupy
Po spuštění skriptu budou zobrazeny následující informace:
Původní data: Předzpracovaná tabulka s pár řádky původních načtených dat.
Předzpracovaná data: Tabulka s pár řádky dat po předzpracování.
Detekované anomálie: Tabulka obsahující řádky, které byly detekovány jako anomálie algoritmem Isolation Forest.

Poznámka:Ujistěte se, že měníte pouze implementaci funkcí preprocess_data() a detect_anomalies() ve skriptu script.py. Při jakýchkoli úpravách nezapomeňte uložit soubory a spustit skript znovu.

Poznámka: Nahraďte `<file_path>` odpovídajícími skutečnými cestami k souborům a provedenými 

## Automatizace scriptu
**Windows (task scheluder)**
1.  Otevřete Task Scheluder z nabídky start.
2.  Klikněte na "Create Basic task" or "Create task" (Záleží na vaší verzi Windows).
