import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_phones(base_url, page_no, dataframe_name):
    all_dataframes = []
    Product_Name = []
    Prices = []
    ROM = []
    Display = []
    Camera = []
    Processor = []
    Warranty = []

    for i in range(2, page_no + 2):
        current_url = base_url.format(i)
        r = requests.get(current_url)
        soup = BeautifulSoup(r.text, "lxml")

        names = soup.find_all("div", class_="_4rR01T")
        prices = soup.find_all("div", class_="_30jeq3 _1_WHN1")
        descriptions = soup.find_all("div", class_="fMghEO")
        
        if r.status_code == 500:
            print(f"Internal Server Error (500) for {current_url}. Skipping this page.")
            continue

        for name, price, description in zip(names, prices, descriptions):
            Product_Name.append(name.text)
            Prices.append(price.text)
            ROM.append(description.find("li", string=lambda s: "ROM" in s).text.strip() if description.find("li", string=lambda s: "ROM" in s) else "")
            Display.append(description.find("li", string=lambda s: "Display" in s).text.strip() if description.find("li", string=lambda s: "Display" in s) else "")
            Camera.append(description.find("li", string=lambda s: "Camera" in s).text.strip() if description.find("li", string=lambda s: "Camera" in s) else "")
            Processor.append(description.find("li", string=lambda s: "Processor" in s).text.strip() if description.find("li", string=lambda s: "Processor" in s) else "")
            Warranty.append(description.find("li", string=lambda s: "Warranty" in s).text.strip() if description.find("li", string=lambda s: "Warranty" in s) else "")
          # Add this before creating the DataFrame
        print(f"Length of Product_Name: {len(Product_Name)}")
        print(f"Length of Prices: {len(Prices)}")
        print(f"Length of ROM: {len(ROM)}")
        print(f"Length of Display: {len(Display)}")
        print(f"Length of Camera: {len(Camera)}")
        print(f"Length of Processor: {len(Processor)}")
        print(f"Length of Warranty: {len(Warranty)}")
    # Check if all arrays have the same length
    array_lengths = [len(Product_Name), len(Prices), len(ROM), len(Display), len(Camera), len(Processor), len(Warranty)]
    if len(set(array_lengths)) != 1:
        print(f"Arrays have inconsistent lengths. Skipping the creation of DataFrame.")
    else:
        df = pd.DataFrame({
            "Product Name": Product_Name,
            "Prices": Prices,
            "ROM": ROM,
            "Display": Display,
            "Camera": Camera,
            "Processor": Processor,
            "Warranty": Warranty
        })

    df['Prices'] = pd.to_numeric(df['Prices'].replace('[^\d.]', '', regex=True), errors='coerce')
    df = df.sort_values(by=['Prices'])

    all_dataframes.append(df)
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_excel(f"E:/FINAL/{dataframe_name}.xlsx", index=False)

# Example usage
scrape_flipkart_phones("https://www.flipkart.com/search?q=i+phones&otracker=AS_Query_HistoryAutoSuggest_2_0&otracker1=AS_Query_HistoryAutoSuggest_2_0&marketplace=FLIPKART&as-show=on&as=off&as-pos=2&as-type=HISTORY&page={}", 10, "i_phones")
scrape_flipkart_phones("https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.serviceability%5B%5D%3Dfalse&p%5B%5D=facets.brand%255B%255D%3DVivo&otracker=nmenu_sub_Electronics_0_Vivo&page={}", 10, "vivo" )
scrape_flipkart_phones("https://www.flipkart.com/mobiles/mi~brand/pr?sid=tyy%2C4io&otracker=nmenu_sub_Electronics_0_Mi&page={}", 10, "mi")
scrape_flipkart_phones("https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=nmenu_sub_Electronics_0_Realme&page={}", 10, "realme")
scrape_flipkart_phones("https://www.flipkart.com/search?p%5B%5D=facets.brand%255B%255D%3DSamsung&sid=tyy%2F4io&sort=recency_desc&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkxhdGVzdCBTYW1zdW5nIG1vYmlsZXMgIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&wid=1.productCard.PMU_V2_1&page={}", 10, "samsung")
scrape_flipkart_phones("https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&otracker=categorytree&p%5B%5D=facets.brand%255B%255D%3DInfinix&otracker=nmenu_sub_Electronics_0_Infinix&page={}", 10, "Infinix")

scrape_flipkart_phones("https://www.flipkart.com/search?count=40&otracker=CLP_filters&otracker=nmenu_sub_Electronics_0_OPPO&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&p%5B%5D=facets.brand%255B%255D%3DOPPO&p%5B%5D=facets.price_range.from%3D20000&p%5B%5D=facets.price_range.to%3DMax&sid=tyy%2F4io&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIk9wcG8gTW9iaWxlcyBhYm92ZSDigrkyMEsiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19&wid=4.productCard.PMU_V2_4&page={}", 10, "oppo")
scrape_flipkart_phones("https://www.flipkart.com/search?p%5B%5D=facets.brand%255B%255D%3DHonor&sid=tyy%2F4io&otracker=CLP_filters&otracker=nmenu_sub_Electronics_0_Honor&page={}", 10, "honor")
scrape_flipkart_phones("https://www.flipkart.com/search?q=poco+x2&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=poco+x2%7CMobiles&requestId=408349ea-12b0-4080-8082-5a58a60f6e52&as-backfill=on&otracker=nmenu_sub_Electronics_0_Poco+X2&page={}", 10, "pocco")
scrape_flipkart_phones("https://www.flipkart.com/search?q=motorola+mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&otracker=nmenu_sub_Electronics_0_Motorola+razr&page={}", 10, "motorola")
scrape_flipkart_phones("https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DAsus&otracker=nmenu_sub_Electronics_0_Asus&page={}", 10, "asus")




# Read Excel files using pd.read_excel()
df_i_phones = pd.read_excel("E:/FINAL/i_phones.xlsx")
df_vivo = pd.read_excel("E:/FINAL/vivo.xlsx")
df_mi = pd.read_excel("E:/FINAL/mi.xlsx")
df_realme = pd.read_excel("E:/FINAL/realme.xlsx")
df_samsung = pd.read_excel("E:/FINAL/samsung.xlsx")
df_Infinix = pd.read_excel("E:/FINAL/Infinix.xlsx")
df_oppo = pd.read_excel("E:/FINAL/oppo.xlsx")
df_honor = pd.read_excel("E:/FINAL/honor.xlsx")
df_pocco = pd.read_excel("E:/FINAL/pocco.xlsx")
df_motorola = pd.read_excel("E:/FINAL/motorola.xlsx")
df_asus = pd.read_excel("E:/FINAL/asus.xlsx")

# Concatenate DataFrames
combined_df = pd.concat([df_i_phones, df_vivo, df_mi, df_realme, df_samsung, df_Infinix,df_oppo,df_honor,df_pocco,df_motorola,df_asus], ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv("E:/FINAL/Combined_data_phones.csv", index=False)




import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_tv(base_url, page_no, dataframe_name):
    all_dataframes = []
    Product_Name = []
    Prices1 = []
    Operating_System = []
    Pixels = []
    Launch_Year = []
    Warranty1 = []

    for i in range(2, page_no + 2):
        current_url = base_url.format(i)
        r = requests.get(current_url)
        soup = BeautifulSoup(r.text, "lxml")

        names = soup.find_all("div", class_="_4rR01T")
        prices = soup.find_all("div", class_="_30jeq3 _1_WHN1")
        descriptions = soup.find_all("div", class_="fMghEO")
        
        if r.status_code == 500:
            print(f"Internal Server Error (500) for {current_url}. Skipping this page.")
            continue

        for name, price, description in zip(names, prices, descriptions):
            Product_Name.append(name.text)
            Prices1.append(price.text)
            Operating_System.append(description.find("li", string=lambda s: "Operating" in s).text.strip() if description.find("li", string=lambda s: " Operating" in s) else "")
            Pixels.append(description.find("li", string=lambda s: "Pixels" in s).text.strip() if description.find("li", string=lambda s: "Pixels" in s) else "")
            Launch_Year.append(description.find("li", string=lambda s: "Launch Year" in s).text.strip() if description.find("li", string=lambda s: "Launch Year" in s) else "")
            Warranty1.append(description.find("li", string=lambda s: "Warranty" in s).text.strip() if description.find("li", string=lambda s: "Warranty" in s) else "")
          # Add this before creating the DataFrame
        print(f"Length of Product Name: {len(Product_Name)}")
        print(f"Length of Prices1: {len(Prices1)}")
        print(f"Length of  Operating: {len( Operating_System)}")
        print(f"Length of Pixels: {len(Pixels)}")
        print(f"Length of Launch Year: {len(Launch_Year)}")
        print(f"Length of Warranty: {len(Warranty1)}")
    # Check if all arrays have the same length
    array_lengths = [len(Product_Name), len(Prices1), len( Operating_System), len(Pixels), len(Launch_Year), len(Warranty1)]
    if len(set(array_lengths)) != 1:
        print(f"Arrays have inconsistent lengths. Skipping the creation of DataFrame.")
    else:
        df = pd.DataFrame({
            "Product Name": Product_Name,
            "Prices1": Prices1,
            "Operating":  Operating_System,
            "Pixels": Pixels,
            "Launch Year": Launch_Year,
            "Warranty": Warranty1
        })

    df['Prices1'] = pd.to_numeric(df['Prices1'].replace('[^\d.]', '', regex=True), errors='coerce')
    df = df.sort_values(by=['Prices1'])

    all_dataframes.append(df)
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_excel(f"E:/FINAL/{dataframe_name}.xlsx", index=False)

# Example usage
scrape_flipkart_tv("https://www.flipkart.com/televisions/pr?sid=ckf%2Cczl&p%5B%5D=facets.brand%255B%255D%3DMi&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=nmenu_sub_TVs+%26+Appliances_0_Mi&page={}", 2, "MITV")
scrape_flipkart_tv("https://www.flipkart.com/televisions/pr?sid=ckf%2Cczl&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.brand%255B%255D%3DThomson&otracker=nmenu_sub_TVs+%26+Appliances_0_Thomson&page={}", 2, "thomson" )
scrape_flipkart_tv("https://www.flipkart.com/televisions/pr?sid=ckf%2Cczl&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.brand%255B%255D%3DSamsung&otracker=nmenu_sub_TVs+%26+Appliances_0_Samsung&page={}", 4, "SamsungTV")
scrape_flipkart_tv("https://www.flipkart.com/search?q=nokia+tv&sid=ckf%2Cczl&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_ps&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_ps&as-pos=1&as-type=RECENT&suggestionId=nokia+tv%7CTelevisions&requestId=62e60a0c-4ff5-4b7f-aec7-df5241a0e2c5&as-backfill=on&otracker=nmenu_sub_TVs+%26+Appliances_0_Nokia&page={}", 50, "nokia")
scrape_flipkart_tv("https://www.flipkart.com/televisions/pr?sid=ckf%2Cczl&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&otracker=categorytree&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&p%5B%5D=facets.brand%255B%255D%3DLG&otracker=nmenu_sub_TVs+%26+Appliances_0_LG&page={}", 2, "LG")




# Read Excel files using pd.read_excel()
df_MITV = pd.read_excel("E:/FINAL/MITV.xlsx")
df_thomson = pd.read_excel("E:/FINAL/thomson.xlsx")
df_SamsungTV = pd.read_excel("E:/FINAL/SamsungTV.xlsx")
df_nokia = pd.read_excel("E:/FINAL/nokia.xlsx")
df_LG = pd.read_excel("E:/FINAL/LG.xlsx")


# Concatenate DataFrames
combined_df = pd.concat([df_thomson, df_nokia,df_MITV,df_SamsungTV,df_LG], ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv("E:/FINAL/Combined_data_TV.csv", index=False)





import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_washingmac(base_url, page_no, dataframe_name):
    all_dataframes = []
    Product_Name = []
    Prices = []
    rpm = []
    Warranty = []

    for i in range(2, page_no + 2):
        current_url = base_url.format(i)
        r = requests.get(current_url)
        soup = BeautifulSoup(r.text, "lxml")

        names = soup.find_all("div", class_="_4rR01T")
        prices = soup.find_all("div", class_="_30jeq3 _1_WHN1")
        descriptions = soup.find_all("div", class_="fMghEO")
        
        if r.status_code == 500:
            print(f"Internal Server Error (500) for {current_url}. Skipping this page.")
            continue

        for name, price, description in zip(names, prices, descriptions):
            Product_Name.append(name.text)
            Prices.append(price.text)
            rpm .append(description.find("li", string=lambda s: "rpm " in s).text.strip() if description.find("li", string=lambda s: "rpm " in s) else "")
            Warranty.append(description.find("li", string=lambda s: "Warranty" in s).text.strip() if description.find("li", string=lambda s: "Warranty" in s) else "")
          # Add this before creating the DataFrame
        print(f"Length of Product_Name: {len(Product_Name)}")
        print(f"Length of Prices: {len(Prices)}")
        print(f"Length of rpm : {len(rpm )}")
        print(f"Length of Warranty: {len(Warranty)}")
    # Check if all arrays have the same length
    array_lengths = [len(Product_Name), len(Prices), len(rpm ), len(Warranty)]
    if len(set(array_lengths)) != 1:
        print(f"Arrays have inconsistent lengths. Skipping the creation of DataFrame.")
    else:
        df = pd.DataFrame({
            "Product Name": Product_Name,
            "Prices": Prices,
            "rpm ": rpm ,
            "Warranty": Warranty
        })

    df['Prices'] = pd.to_numeric(df['Prices'].replace('[^\d.]', '', regex=True), errors='coerce')
    df = df.sort_values(by=['Prices'])

    all_dataframes.append(df)
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_excel(f"E:/FINAL/{dataframe_name}.xlsx", index=False)

# Example usage
scrape_flipkart_washingmac("https://www.flipkart.com/home-kitchen/home-appliances/washing-machines/fully-automatic-front-load~function/pr?sid=j9e%2Cabm%2C8qx&otracker=nmenu_sub_TVs+%26+Appliances_0_Fully+Automatic+Front+Load&page={}",10,"Fullyautofront")
scrape_flipkart_washingmac("https://www.flipkart.com/home-kitchen/home-appliances/washing-machines/semi-automatic-top-load~function/pr?sid=j9e%2Cabm%2C8qx&otracker=nmenu_sub_TVs+%26+Appliances_0_Semi+Automatic+Top+Load&page={}",10,"Semiautotop")
scrape_flipkart_washingmac("https://www.flipkart.com/home-kitchen/home-appliances/washing-machines/fully-automatic-top-load~function/pr?sid=j9e%2Cabm%2C8qx&otracker=nmenu_sub_TVs+%26+Appliances_0_Fully+Automatic+Top+Load&page={}",10,"Fullyautotop")

# Read Excel files using pd.read_excel()
df_Fullyautofront = pd.read_excel("E:/FINAL/Fullyautofront.xlsx")
df_Semiautotop= pd.read_excel("E:/FINAL/Semiautotop.xlsx")
df_Fullyautotop = pd.read_excel("E:/FINAL/Fullyautotop.xlsx")


# Concatenate DataFrames
combined_df = pd.concat([df_Fullyautofront, df_Semiautotop, df_Fullyautotop ], ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv("E:/FINAL/Combined_data_Washing_Machine.csv", index=False)



import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_ref(base_url, page_no, dataframe_name):
    all_dataframes = []
    Product_Name = []
    Prices = []
    Compressor = []
    Built_in = []
    Warranty = []

    for i in range(2, page_no + 2):
        current_url = base_url.format(i)
        r = requests.get(current_url)
        soup = BeautifulSoup(r.text, "lxml")

        names = soup.find_all("div", class_="_4rR01T")
        prices = soup.find_all("div", class_="_30jeq3 _1_WHN1")
        descriptions = soup.find_all("div", class_="fMghEO")
        
        if r.status_code == 500:
            print(f"Internal Server Error (500) for {current_url}. Skipping this page.")
            continue

        for name, price, description in zip(names, prices, descriptions):
            Product_Name.append(name.text)
            Prices.append(price.text)
            Compressor.append(description.find("li", string=lambda s: "Compressor" in s).text.strip() if description.find("li", string=lambda s: "Compressor" in s) else "")
            Built_in.append(description.find("li", string=lambda s: "Built-in" in s).text.strip() if description.find("li", string=lambda s: "Built-in" in s) else "")
            Warranty.append(description.find("li", string=lambda s: "Warranty" in s).text.strip() if description.find("li", string=lambda s: "Warranty" in s) else "")
          # Add this before creating the DataFrame
        print(f"Length of Product_Name: {len(Product_Name)}")
        print(f"Length of Prices: {len(Prices)}")
        print(f"Length of Compressor: {len(Compressor)}")
        print(f"Length of Built-in: {len(Built_in)}")
        print(f"Length of Warranty: {len(Warranty)}")
    # Check if all arrays have the same length
    array_lengths = [len(Product_Name), len(Prices), len(Compressor), len(Built_in), len(Warranty)]
    if len(set(array_lengths)) != 1:
        print(f"Arrays have inconsistent lengths. Skipping the creation of DataFrame.")
    else:
        df = pd.DataFrame({
            "Product Name": Product_Name,
            "Prices": Prices,
            "Compressor": Compressor,
            "Built-in": Built_in,
            "Warranty": Warranty
        })

    df['Prices'] = pd.to_numeric(df['Prices'].replace('[^\d.]', '', regex=True), errors='coerce')
    df = df.sort_values(by=['Prices'])

    all_dataframes.append(df)
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_excel(f"E:/FINAL/{dataframe_name}.xlsx", index=False)

# Example usage
scrape_flipkart_ref("https://www.flipkart.com/home-kitchen/home-appliances/refrigerators/single-door~type/pr?sid=j9e%2Cabm%2Chzg&otracker=nmenu_sub_TVs+%26+Appliances_0_Single+Door&page={}", 30, "singledoor")
scrape_flipkart_ref("https://www.flipkart.com/home-kitchen/home-appliances/refrigerators/double-door~type/pr?sid=j9e%2Cabm%2Chzg&otracker=nmenu_sub_TVs+%26+Appliances_0_Double+Door&page={}", 40, "doubledoor" )
scrape_flipkart_ref("https://www.flipkart.com/home-kitchen/home-appliances/refrigerators/double-door~type/pr?sid=j9e%2Cabm%2Chzg&otracker=nmenu_sub_TVs+%26+Appliances_0_Double+Door&page={}", 10, "tripledoor")
scrape_flipkart_ref("https://www.flipkart.com/home-kitchen/home-appliances/refrigerators/pr?otracker=categorytree&p%5B%5D=facets.type%255B%255D%3DSide%2Bby%2BSide&sid=j9e%2Fabm%2Fhzg&otracker=nmenu_sub_TVs+%26+Appliances_0_Side+by+Side&page={}", 50, "sidebyside")
scrape_flipkart_ref("https://www.flipkart.com/search?p%5B%5D%5B%5D=facets.features%255B%255D%3DConvertible&sid=j9e%2Fabm%2Fhzg&otracker=CLP_filters&p%5B%5D=facets.features%255B%255D%3DConvertible&otracker=nmenu_sub_TVs+%26+Appliances_0_Convertible&page={}", 50, "convertible")






# Read Excel files using pd.read_excel()
df_singledoor = pd.read_excel("E:/FINAL/singledoor.xlsx")
df_doubledoor = pd.read_excel("E:/FINAL/doubledoor.xlsx")
df_tripledoor = pd.read_excel("E:/FINAL/tripledoor.xlsx")
df_sidebyside = pd.read_excel("E:/FINAL/sidebyside.xlsx")
df_convertible = pd.read_excel("E:/FINAL/convertible.xlsx")

# df_oppo = pd.read_excel("E:/FINAL/oppo.xlsx")
# df_honor = pd.read_excel("E:/FINAL/honor.xlsx")
# df_pocco = pd.read_excel("E:/FINAL/pocco.xlsx")
# df_motorola = pd.read_excel("E:/FINAL/motorola.xlsx")
# df_asus = pd.read_excel("E:/FINAL/asus.xlsx")

# Concatenate DataFrames
combined_df = pd.concat([df_singledoor,df_doubledoor, df_tripledoor,df_sidebyside,df_convertible], ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv("E:/FINAL/Combined_data_refrigerators.csv", index=False)

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_ac(base_url, page_no, dataframe_name):
    all_dataframes = []
    Product_Name = []
    Prices = []
    Annual_Power = []
    Room_Size = []
    Warranty = []

    for i in range(2, page_no + 2):
        current_url = base_url.format(i)
        r = requests.get(current_url)
        soup = BeautifulSoup(r.text, "lxml")

        names = soup.find_all("div", class_="_4rR01T")
        prices = soup.find_all("div", class_="_30jeq3 _1_WHN1")
        descriptions = soup.find_all("div", class_="fMghEO")
        
        if r.status_code == 500:
            print(f"Internal Server Error (500) for {current_url}. Skipping this page.")
            continue

        for name, price, description in zip(names, prices, descriptions):
            Product_Name.append(name.text)
            Prices.append(price.text)
            Annual_Power.append(description.find("li", string=lambda s: "Annual Power" in s).text.strip() if description.find("li", string=lambda s: "Annual Power" in s) else "")
            Room_Size.append(description.find("li", string=lambda s: "Room Size" in s).text.strip() if description.find("li", string=lambda s: "Room Size" in s) else "")
            Warranty.append(description.find("li", string=lambda s: "Warranty" in s).text.strip() if description.find("li", string=lambda s: "Warranty" in s) else "")
          # Add this before creating the DataFrame
        print(f"Length of Product_Name: {len(Product_Name)}")
        print(f"Length of Prices: {len(Prices)}")
        print(f"Length of Annual Power: {len(Annual_Power)}")
        print(f"Length of Room Size: {len(Room_Size)}")
        print(f"Length of Warranty: {len(Warranty)}")
    # Check if all arrays have the same length
    array_lengths = [len(Product_Name), len(Prices), len(Annual_Power), len(Room_Size), len(Warranty)]
    if len(set(array_lengths)) != 1:
        print(f"Arrays have inconsistent lengths. Skipping the creation of DataFrame.")
    else:
        df = pd.DataFrame({
            "Product Name": Product_Name,
            "Prices": Prices,
            "Annual Power": Annual_Power,
            "Room Size": Room_Size,
            "Warranty": Warranty
        })

    df['Prices'] = pd.to_numeric(df['Prices'].replace('[^\d.]', '', regex=True), errors='coerce')
    df = df.sort_values(by=['Prices'])

    all_dataframes.append(df)
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_excel(f"E:/FINAL/{dataframe_name}.xlsx", index=False)

# Example usage
scrape_flipkart_ac("https://www.flipkart.com/air-conditioners/pr?sid=j9e%2Cabm%2Cc54&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p%5B%5D=facets.technology%255B%255D%3DInverter&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&otracker=categorytree&otracker=nmenu_sub_TVs+%26+Appliances_0_Inverter+AC&page={}", 40, "inverterac")
scrape_flipkart_ac("https://www.flipkart.com/home-kitchen/home-appliances/air-conditioners/split~type/pr?sid=j9e%2Cabm%2Cc54&otracker=nmenu_sub_TVs+%26+Appliances_0_Split+ACs&page={}", 40, "splitac" )
scrape_flipkart_ac("https://www.flipkart.com/home-kitchen/home-appliances/air-conditioners/window~type/pr?sid=j9e%2Cabm%2Cc54&otracker=nmenu_sub_TVs+%26+Appliances_0_Window+ACs&page={}", 40, "windowac")

# Read Excel files using pd.read_excel()
df_inverterac = pd.read_excel("E:/FINAL/inverterac.xlsx")
df_splitac = pd.read_excel("E:/FINAL/splitac.xlsx")
df_windowac = pd.read_excel("E:/FINAL/windowac.xlsx")


# Concatenate DataFrames
combined_df = pd.concat([df_inverterac,df_splitac,df_windowac], ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv("E:/FINAL/Combined_data_ac.csv", index=False)



import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_laptop(base_url, page_no, dataframe_name):
    all_dataframes = []
    Product_Name = []
    Prices = []
    Processor = []
    RAM = []
    Operating_System = []
    SSD = []
    Display =[]
    Warranty = []

    for i in range(2, page_no + 2):
        current_url = base_url.format(i)
        r = requests.get(current_url)
        soup = BeautifulSoup(r.text, "lxml")

        names = soup.find_all("div", class_="_4rR01T")
        prices = soup.find_all("div", class_="_30jeq3 _1_WHN1")
        descriptions = soup.find_all("div", class_="fMghEO")
        
        if r.status_code == 500:
            print(f"Internal Server Error (500) for {current_url}. Skipping this page.")
            continue

        for name, price, description in zip(names, prices, descriptions):
            Product_Name.append(name.text)
            Prices.append(price.text)
            Processor.append(description.find("li", string=lambda s: "Processor" in s).text.strip() if description.find("li", string=lambda s: "Processor" in s) else "")
            RAM.append(description.find("li", string=lambda s: "RAM" in s).text.strip() if description.find("li", string=lambda s: "RAM" in s) else "")
            Operating_System.append(description.find("li", string=lambda s: "Operating System" in s).text.strip() if description.find("li", string=lambda s: "Operating System" in s) else "")
            SSD.append(description.find("li", string=lambda s: "SSD" in s).text.strip() if description.find("li", string=lambda s: "SSD" in s) else "")
            Display.append(description.find("li", string=lambda s: "Display" in s).text.strip() if description.find("li", string=lambda s: "Display" in s) else "")
            Warranty.append(description.find("li", string=lambda s: "Warranty" in s).text.strip() if description.find("li", string=lambda s: "Warranty" in s) else "")
          # Add this before creating the DataFrame
        print(f"Length of Product_Name: {len(Product_Name)}")
        print(f"Length of Prices: {len(Prices)}")
        print(f"Length of Processor: {len(Processor)}")
        print(f"Length of RAM: {len(RAM)}")
        print(f"Length of Operating System: {len(Operating_System)}")
        print(f"Length of Display: {len(Display)}")
        print(f"Length of SSD: {len(SSD)}")
        print(f"Length of Warranty: {len(Warranty)}")
    # Check if all arrays have the same length
    array_lengths = [len(Product_Name), len(Prices),len(Processor), len(RAM), len(Operating_System), len(Display), len(SSD), len(Warranty)]
    if len(set(array_lengths)) != 1:
        print(f"Arrays have inconsistent lengths. Skipping the creation of DataFrame.")
    else:
        df = pd.DataFrame({
            "Product Name": Product_Name,
            "Prices": Prices,
            "Processor": Processor,
            "RAM": RAM,
            "Display": Display,
            "Operating System": Operating_System,
            "SSD": SSD,
            "Warranty": Warranty
            })

    df['Prices'] = pd.to_numeric(df['Prices'].replace('[^\d.]', '', regex=True), errors='coerce')
    df = df.sort_values(by=['Prices'])

    all_dataframes.append(df)
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_excel(f"E:/FINAL/{dataframe_name}.xlsx", index=False)

# Example usage
scrape_flipkart_laptop("https://www.flipkart.com/computers/laptops/pr?sid=6bo%2Cb5g&sort=price_asc&p%5B%5D=facets.type%255B%255D%3DGaming%2BLaptop&p%5B%5D=facets.brand%255B%255D%3DAcer&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkFjZXIgR2FtaW5nIExhcHRvcHMiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19&wid=3.productCard.PMU_V2_2&page={}", 10, "acer")
scrape_flipkart_laptop("https://www.flipkart.com/laptops/pr?sid=6bo%2Cb5g&p%5B%5D=facets.brand%255B%255D%3DLenovo&p%5B%5D=facets.type%255B%255D%3DGaming%2BLaptop&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkxlbm92byBHYW1pbmcgTGFwdG9wcyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D&wid=4.productCard.PMU_V2_3&page={}", 20, "lenovo" )
scrape_flipkart_laptop("https://www.flipkart.com/computers/laptops/~asus-gaming-laptops21/pr?sid=6bo%2Cb5g&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkFzdXMgR2FtaW5nIExhcHRvcHMiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19&wid=5.productCard.PMU_V2_4&page={}",40, "asusl")
scrape_flipkart_laptop("https://www.flipkart.com/computers/laptops/~msi-gaming-laptops/pr?sid=6bo%2Cb5g&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIk1TSSBHYW1pbmcgTGFwdG9wcyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D&wid=6.productCard.PMU_V2_5&page={}", 10, "msi")
scrape_flipkart_laptop("https://www.flipkart.com/computers/laptops/~dell-gaming-laptops21/pr?sid=6bo%2Cb5g&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkRlbGwgR2FtaW5nIExhcHRvcHMiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19fX19&wid=9.productCard.PMU_V2_6&page={}", 40, "dell")





# Read Excel files using pd.read_excel()
df_acer = pd.read_excel("E:/FINAL/acer.xlsx")
df_lenovo= pd.read_excel("E:/FINAL/lenovo.xlsx")
df_asusl = pd.read_excel("E:/FINAL/asusl.xlsx")
df_msi = pd.read_excel("E:/FINAL/msi.xlsx")
df_dell = pd.read_excel("E:/FINAL/dell.xlsx")


# Concatenate DataFrames
combined_df = pd.concat([df_acer,df_lenovo, df_asusl, df_msi,df_dell], ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv("E:/FINAL/Combined_data_laptops.csv", index=False)

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_purifier(base_url, page_no, dataframe_name):
    all_dataframes = []
    Product_Name = []
    Prices = []
    Filtration_Capacity =[]
    Warranty = []

    for i in range(2, page_no + 2):
        current_url = base_url.format(i)
        r = requests.get(current_url)
        soup = BeautifulSoup(r.text, "lxml")

        names = soup.find_all("div", class_="_4rR01T")
        prices = soup.find_all("div", class_="_30jeq3 _1_WHN1")
        descriptions = soup.find_all("div", class_="fMghEO")
        
        if r.status_code == 500:
            print(f"Internal Server Error (500) for {current_url}. Skipping this page.")
            continue

        for name, price, description in zip(names, prices, descriptions):
            Product_Name.append(name.text)
            Prices.append(price.text)
            Filtration_Capacity.append(description.find("li", string=lambda s: "Filtration Capacity" in s).text.strip() if description.find("li", string=lambda s: "Filtration Capacity" in s) else "")
            Warranty.append(description.find("li", string=lambda s: "Warranty" in s).text.strip() if description.find("li", string=lambda s: "Warranty" in s) else "")
          # Add this before creating the DataFrame
        print(f"Length of Product_Name: {len(Product_Name)}")
        print(f"Length of Prices: {len(Prices)}")
        print(f"Length of Filtration Capacity: {len(Filtration_Capacity)}")
        print(f"Length of Warranty: {len(Warranty)}")
    # Check if all arrays have the same length
    array_lengths = [len(Product_Name), len(Prices),len(Filtration_Capacity),len(Warranty)]
    if len(set(array_lengths)) != 1:
        print(f"Arrays have inconsistent lengths. Skipping the creation of DataFrame.")
    else:
        df = pd.DataFrame({
            "Product Name": Product_Name,
            "Prices": Prices,
            "Filtration Capacity": Filtration_Capacity,
            "Warranty": Warranty
            })

    df['Prices'] = pd.to_numeric(df['Prices'].replace('[^\d.]', '', regex=True), errors='coerce')
    df = df.sort_values(by=['Prices'])

    all_dataframes.append(df)
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_excel(f"E:/FINAL/{dataframe_name}.xlsx", index=False)

# Example usage
scrape_flipkart_purifier("https://www.flipkart.com/home-kitchen/home-appliances/water-purifiers/pr?sid=j9e%2Cabm%2Ci45&p%5B%5D=facets.fulfilled_by%255B%255D%3DPlus%2B%2528FAssured%2529&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.offer_type%255B%255D%3DSpecial%2BPrice&hpid=nq1lWbcCvEp-1C3LRBWMg6p7_Hsxr70nj65vMAAFKlc%3D&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJTaG9wIE5vdyEiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJoZXJvUGlkIjp7InNpbmdsZVZhbHVlQXR0cmlidXRlIjp7ImtleSI6Imhlcm9QaWQiLCJpbmZlcmVuY2VUeXBlIjoiUElEIiwidmFsdWUiOiJXQVBGSkhZV0JZVllLVVZNIiwidmFsdWVUeXBlIjoiU0lOR0xFX1ZBTFVFRCJ9fSwidGl0bGUiOnsibXVsdGlWYWx1ZWRBdHRyaWJ1dGUiOnsia2V5IjoidGl0bGUiLCJpbmZlcmVuY2VUeXBlIjoiVElUTEUiLCJ2YWx1ZXMiOlsiVG9wIFdhdGVyIFB1cmlmaWVycyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D&fm=neo%2Fmerchandising&iid=M_9f2fcd1d-9ad3-4b35-850f-9128e9f41ba1_1.TW0VOZRZV2M9&ppt=browse&ppn=browse&ssid=qap6x0enk00000001710307509673&otracker=dynamic_omu_infinite_Best%2BDeals%2BOn%2BAppliances_5_1.dealCard.OMU_INFINITE_TW0VOZRZV2M9&cid=TW0VOZRZV2M9&page={}", 210, "water_purifier")






# Read Excel files using pd.read_excel()
df_water_purifier= pd.read_excel("E:/FINAL/water_purifier.xlsx")



# Concatenate DataFrames
combined_df = pd.concat([df_water_purifier], ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv("E:/FINAL/Combined_data_water_purifier.csv", index=False)




import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_oven(base_url, page_no, dataframe_name):
    all_dataframes = []
    Product_Name = []
    Prices = []
    Control = []
    Child_Lock = []
    Warranty = []

    for i in range(2, page_no + 2):
        current_url = base_url.format(i)
        r = requests.get(current_url)
        soup = BeautifulSoup(r.text, "lxml")

        names = soup.find_all("div", class_="_4rR01T")
        prices = soup.find_all("div", class_="_30jeq3 _1_WHN1")
        descriptions = soup.find_all("div", class_="fMghEO")
        
        if r.status_code == 500:
            print(f"Internal Server Error (500) for {current_url}. Skipping this page.")
            continue
        for name, price, description in zip(names, prices, descriptions):
            Product_Name.append(name.text)
            Prices.append(price.text)

            control_elem = description.find("li", string=lambda s: "Control" in s)
            Control.append(control_elem.text.strip() if control_elem else "")

            child_lock_elem = description.find("li", string=lambda s: "Child Lock" in s)
            Child_Lock.append(child_lock_elem.text.strip() if child_lock_elem else "")

            warranty_elem = description.find("li", string=lambda s: "Warranty" in s)
            Warranty.append(warranty_elem.text.strip() if warranty_elem else "")

# Rest of the code remains unchanged

        print(f"Length of Product_Name: {len(Product_Name)}")
        print(f"Length of Prices: {len(Prices)}")
        print(f"Length of Control: {len(Control)}")
        print(f"Length of Child Lock: {len(Child_Lock)}")
        print(f"Length of Warranty: {len(Warranty)}")
    # Check if all arrays have the same length
    array_lengths = [len(Product_Name), len(Prices), len(Control), len(Child_Lock), len(Warranty)]
    if len(set(array_lengths)) != 1:
        print(f"Arrays have inconsistent lengths. Skipping the creation of DataFrame.")
    else:
        df = pd.DataFrame({
            "Product Name": Product_Name,
            "Prices": Prices,
            "Control Type : ": Control,
            "Child Lock": Child_Lock,
            "Warranty": Warranty
        })

    df['Prices'] = pd.to_numeric(df['Prices'].replace('[^\d.]', '', regex=True), errors='coerce')
    df = df.sort_values(by=['Prices'])

    all_dataframes.append(df)
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_excel(f"E:/FINAL/{dataframe_name}.xlsx", index=False)

# Example usage
scrape_flipkart_oven("https://www.flipkart.com/search?q=microwave+oven&sid=j9e%2Cm38%2Co49&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&as-pos=1&as-type=RECENT&suggestionId=microwave+oven%7CMicrowave+Ovens&requestId=7786a822-b9b3-433c-8d4c-008ae2772f8d&as-backfill=on&otracker=nmenu_sub_TVs+%26+Appliances_0_Microwave+Ovens&page={}", 50, "microwaveoven")
scrape_flipkart_oven("https://www.flipkart.com/search?q=microwave+oven&sid=j9e%2Cm38%2Co49&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_10_na_na_na&as-pos=1&as-type=RECENT&suggestionId=microwave+oven%7CMicrowave+Ovens&requestId=7786a822-b9b3-433c-8d4c-008ae2772f8d&as-backfill=on&otracker=nmenu_sub_TVs+%26+Appliances_0_Microwave+Ovens&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&page={}", 30, "samsungoven" )

# Read Excel files using pd.read_excel()
df_microwaveoven = pd.read_excel("E:/FINAL/microwaveoven.xlsx")
df_samsungoven = pd.read_excel("E:/FINAL/samsungoven.xlsx")



# Concatenate DataFrames
combined_df = pd.concat([df_microwaveoven,df_samsungoven], ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv("E:/FINAL/Combined_data_oven.csv", index=False)



import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_menswear(base_url, page_no, dataframe_name):
    all_dataframes = []
    Product_Name = []
    Prices = []

    for i in range(2, page_no + 2):
        current_url = base_url.format(i)
        r = requests.get(current_url)
        soup = BeautifulSoup(r.text, "lxml")
        names = soup.find_all("div", class_="_2WkVRV")
        prices = soup.find_all("div", class_="_30jeq3")
        if r.status_code == 500:
            print(f"Internal Server Error (500) for {current_url}. Skipping this page.")
            continue
        for name, price in zip(names, prices):
            Product_Name.append(name.text)
            Prices.append(price.text)
# Rest of the code remains unchanged
        print(f"Length of Product_Name: {len(Product_Name)}")
        print(f"Length of Prices: {len(Prices)}")
    array_lengths = [len(Product_Name), len(Prices)]
    if len(set(array_lengths)) != 1:
        print(f"Arrays have inconsistent lengths. Skipping the creation of DataFrame.")
    else:
        df = pd.DataFrame({
            "Product Name": Product_Name,
            "Prices": Prices,
        })

    df['Prices'] = pd.to_numeric(df['Prices'].replace('[^\d.]', '', regex=True), errors='coerce')
    df = df.sort_values(by=['Prices'])

    all_dataframes.append(df)
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_excel(f"E:/FINAL/{dataframe_name}.xlsx", index=False)

# Example usage
scrape_flipkart_menswear("https://www.flipkart.com/clothing-and-accessories/bottomwear/pr?sid=clo%2Cvua&p%5B%5D=facets.ideal_for%255B%255D%3DMen&p%5B%5D=facets.ideal_for%255B%255D%3Dmen&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_0367ae4b-bc95-43d7-9362-0be8bb91f476_1_372UD5BXDFYS_MC.8HARX8UX7IX5&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Fashion%7EMen%2527s%2BBottom%2BWear_8HARX8UX7IX5&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L1_view-all&cid=8HARX8UX7IX5&page={}", 500, "menswear")

# Read Excel files using pd.read_excel()
df_menswear = pd.read_excel("E:/FINAL/menswear.xlsx")

# Concatenate DataFrames
combined_df = pd.concat([df_menswear], ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv("E:/FINAL/Combined_data_menswear.csv", index=False)



import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_mensfootwear(base_url, page_no, dataframe_name):
    all_dataframes = []
    Product_Name = []
    Prices = []

    for i in range(2, page_no + 2):
        current_url = base_url.format(i)
        r = requests.get(current_url)
        soup = BeautifulSoup(r.text, "lxml")
        names = soup.find_all("div", class_="_2WkVRV")
        prices = soup.find_all("div", class_="_30jeq3")
        if r.status_code == 500:
            print(f"Internal Server Error (500) for {current_url}. Skipping this page.")
            continue
        for name, price in zip(names, prices):
            Product_Name.append(name.text)
            Prices.append(price.text)
# Rest of the code remains unchanged
        print(f"Length of Product_Name: {len(Product_Name)}")
        print(f"Length of Prices: {len(Prices)}")
    array_lengths = [len(Product_Name), len(Prices)]
    if len(set(array_lengths)) != 1:
        print(f"Arrays have inconsistent lengths. Skipping the creation of DataFrame.")
    else:
        df = pd.DataFrame({
            "Product Name": Product_Name,
            "Prices": Prices,
        })

    df['Prices'] = pd.to_numeric(df['Prices'].replace('[^\d.]', '', regex=True), errors='coerce')
    df = df.sort_values(by=['Prices'])

    all_dataframes.append(df)
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_excel(f"E:/FINAL/{dataframe_name}.xlsx", index=False)

# Example usage
scrape_flipkart_mensfootwear("https://www.flipkart.com/mens-footwear/casual-shoes/pr?sid=osp%2Ccil%2Ce1f&fm=neo%2Fmerchandising&iid=M_e1da3fe2-ac15-4430-9286-2649db81d32a_1_372UD5BXDFYS_MC.30OZVDNS8SCQ&otracker=hp_rich_navigation_3_1.navigationCard.RICH_NAVIGATION_Fashion%7EMen%2BFootwear%7EMen%2527s%2BCasual%2BShoes_30OZVDNS8SCQ&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L2_view-all&cid=30OZVDNS8SCQ&page={}", 500, "mensfootwear")

# Read Excel files using pd.read_excel()
df_mensfootwear = pd.read_excel("E:/FINAL/mensfootwear.xlsx")

# Concatenate DataFrames
combined_df = pd.concat([df_mensfootwear], ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv("E:/FINAL/Combined_data_mensfootwear.csv", index=False)


import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_watches(base_url, page_no, dataframe_name):
    all_dataframes = []
    Product_Name = []
    Prices = []

    for i in range(2, page_no + 2):
        current_url = base_url.format(i)
        r = requests.get(current_url)
        soup = BeautifulSoup(r.text, "lxml")
        names = soup.find_all("div", class_="_2WkVRV")
        prices = soup.find_all("div", class_="_30jeq3")
        if r.status_code == 500:
            print(f"Internal Server Error (500) for {current_url}. Skipping this page.")
            continue
        for name, price in zip(names, prices):
            Product_Name.append(name.text)
            Prices.append(price.text)
# Rest of the code remains unchanged
        print(f"Length of Product_Name: {len(Product_Name)}")
        print(f"Length of Prices: {len(Prices)}")
    array_lengths = [len(Product_Name), len(Prices)]
    if len(set(array_lengths)) != 1:
        print(f"Arrays have inconsistent lengths. Skipping the creation of DataFrame.")
    else:
        df = pd.DataFrame({
            "Product Name": Product_Name,
            "Prices": Prices,
        })

    df['Prices'] = pd.to_numeric(df['Prices'].replace('[^\d.]', '', regex=True), errors='coerce')
    df = df.sort_values(by=['Prices'])

    all_dataframes.append(df)
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_excel(f"E:/FINAL/{dataframe_name}.xlsx", index=False)

# Example usage
scrape_flipkart_watches("https://www.flipkart.com/watches/wrist-watches/pr?sid=r18%2Cf13&p%5B%5D=facets.ideal_for%255B%255D%3DCouple&p%5B%5D=facets.ideal_for%255B%255D%3DWomen&p%5B%5D=facets.ideal_for%255B%255D%3DMen%2B%2526%2BWomen&p%5B%5D=facets.ideal_for%255B%255D%3DMen&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_e260de78-d3dd-4eca-ab93-c33fbfba78f1_1_372UD5BXDFYS_MC.CI9JK83AKS5H&otracker=hp_rich_navigation_6_1.navigationCard.RICH_NAVIGATION_Fashion%7EWatches%2Band%2BAccessories_CI9JK83AKS5H&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_6_L1_view-all&cid=CI9JK83AKS5H&page={}", 500, "watches")

# Read Excel files using pd.read_excel()
df_watches = pd.read_excel("E:/FINAL/watches.xlsx")

# Concatenate DataFrames
combined_df = pd.concat([df_watches], ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv("E:/FINAL/Combined_data_watches.csv", index=False)



import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_powerbanks(base_url, page_no, dataframe_name):
    all_dataframes = []
    Product_Name = []
    Prices = []

    for i in range(2, page_no + 2):
        current_url = base_url.format(i)
        r = requests.get(current_url)
        soup = BeautifulSoup(r.text, "lxml")
        names = soup.find_all("a", class_="s1Q9rs")
        prices = soup.find_all("div", class_="_30jeq3")
        if r.status_code == 500:
            print(f"Internal Server Error (500) for {current_url}. Skipping this page.")
            continue
        for name, price in zip(names, prices):
            Product_Name.append(name.text)
            Prices.append(price.text)
# Rest of the code remains unchanged
        print(f"Length of Product_Name: {len(Product_Name)}")
        print(f"Length of Prices: {len(Prices)}")
    array_lengths = [len(Product_Name), len(Prices)]
    if len(set(array_lengths)) != 1:
        print(f"Arrays have inconsistent lengths. Skipping the creation of DataFrame.")
    else:
        df = pd.DataFrame({
            "Product Name": Product_Name,
            "Prices": Prices,
        })

    df['Prices'] = pd.to_numeric(df['Prices'].replace('[^\d.]', '', regex=True), errors='coerce')
    df = df.sort_values(by=['Prices'])

    all_dataframes.append(df)
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_excel(f"E:/FINAL/{dataframe_name}.xlsx", index=False)

# Example usage
scrape_flipkart_powerbanks("https://www.flipkart.com/mobile-accessories/power-banks/pr?sid=tyy%2C4mr%2Cfu6&otracker=categorytree&otracker=nmenu_sub_Electronics_0_Power+Banks&fm=neo%2Fmerchandising&iid=M_f6d60300-126e-4dba-aa74-e4aebd91ccaf_1_372UD5BXDFYS_MC.SUDNEM7MT757&otracker=hp_rich_navigation_10_1.navigationCard.RICH_NAVIGATION_Electronics%7EPowerbank_SUDNEM7MT757&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_10_L1_view-all&cid=SUDNEM7MT757&page={}", 100, "powerbanks")

# Read Excel files using pd.read_excel()
df_powerbanks = pd.read_excel("E:/FINAL/powerbanks.xlsx")

# Concatenate DataFrames
combined_df = pd.concat([df_powerbanks], ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv("E:/FINAL/Combined_data_powerbanks.csv", index=False)



import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_bookshelf(base_url, page_no, dataframe_name):
    all_dataframes = []
    Product_Name = []
    Prices = []

    for i in range(2, page_no + 2):
        current_url = base_url.format(i)
        r = requests.get(current_url)
        soup = BeautifulSoup(r.text, "lxml")
        names = soup.find_all("a", class_="s1Q9rs")
        prices = soup.find_all("div", class_="_30jeq3")
        if r.status_code == 500:
            print(f"Internal Server Error (500) for {current_url}. Skipping this page.")
            continue
        for name, price in zip(names, prices):
            Product_Name.append(name.text)
            Prices.append(price.text)
# Rest of the code remains unchanged
        print(f"Length of Product_Name: {len(Product_Name)}")
        print(f"Length of Prices: {len(Prices)}")
    array_lengths = [len(Product_Name), len(Prices)]
    if len(set(array_lengths)) != 1:
        print(f"Arrays have inconsistent lengths. Skipping the creation of DataFrame.")
    else:
        df = pd.DataFrame({
            "Product Name": Product_Name,
            "Prices": Prices,
        })

    df['Prices'] = pd.to_numeric(df['Prices'].replace('[^\d.]', '', regex=True), errors='coerce')
    df = df.sort_values(by=['Prices'])

    all_dataframes.append(df)
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_excel(f"E:/FINAL/{dataframe_name}.xlsx", index=False)

# Example usage
scrape_flipkart_bookshelf("https://www.flipkart.com/furniture/shelves/pr?sid=wwe%2Cvmc&hpid=YuDPfy3AGeX6pQHclNyN5Kp7_Hsxr70nj65vMAAFKlc%3D&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJGcm9tIOKCuTEsOTk5Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fSwiaGVyb1BpZCI6eyJzaW5nbGVWYWx1ZUF0dHJpYnV0ZSI6eyJrZXkiOiJoZXJvUGlkIiwiaW5mZXJlbmNlVHlwZSI6IlBJRCIsInZhbHVlIjoiQlNGRkdQSjMyVU5TU1VUSCIsInZhbHVlVHlwZSI6IlNJTkdMRV9WQUxVRUQifX0sInRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkJvb2sgU2hlbGZzIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&fm=neo%2Fmerchandising&iid=M_0f0c529c-639e-43a1-b4af-0bf269fcc026_1.DWRGWQISZZJC&ppt=clp&ppn=furniture-india-ka-furniture-bedroom-store&ssid=i1jnj8drk00000001711458884360&otracker=dynamic_omu_infinite_Bedroom%2BFurniture_6_1.dealCard.OMU_INFINITE_DWRGWQISZZJC&cid=DWRGWQISZZJC&page={}", 400, "bookshelf")

# Read Excel files using pd.read_excel()
df_bookshelf = pd.read_excel("E:/FINAL/bookshelf.xlsx")

# Concatenate DataFrames
combined_df = pd.concat([df_bookshelf], ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv("E:/FINAL/Combined_data_bookshelf.csv", index=False)


import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_bed(base_url, page_no, dataframe_name):
    all_dataframes = []
    Product_Name = []
    Prices = []

    for i in range(2, page_no + 2):
        current_url = base_url.format(i)
        r = requests.get(current_url)
        soup = BeautifulSoup(r.text, "lxml")
        names = soup.find_all("a", class_="s1Q9rs")
        prices = soup.find_all("div", class_="_30jeq3")
        if r.status_code == 500:
            print(f"Internal Server Error (500) for {current_url}. Skipping this page.")
            continue
        for name, price in zip(names, prices):
            Product_Name.append(name.text)
            Prices.append(price.text)
# Rest of the code remains unchanged
        print(f"Length of Product_Name: {len(Product_Name)}")
        print(f"Length of Prices: {len(Prices)}")
    array_lengths = [len(Product_Name), len(Prices)]
    if len(set(array_lengths)) != 1:
        print(f"Arrays have inconsistent lengths. Skipping the creation of DataFrame.")
    else:
        df = pd.DataFrame({
            "Product Name": Product_Name,
            "Prices": Prices,
        })

    df['Prices'] = pd.to_numeric(df['Prices'].replace('[^\d.]', '', regex=True), errors='coerce')
    df = df.sort_values(by=['Prices'])

    all_dataframes.append(df)
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_excel(f"E:/FINAL/{dataframe_name}.xlsx", index=False)

# Example usage
scrape_flipkart_bed("https://www.flipkart.com/furniture/beds-more/beds/pr?sid=wwe%2C7p7%2C4yf&otracker=categorytree&p%5B%5D=facets.price_range.from%3D1500&p%5B%5D=facets.price_range.to%3DMax&fm=neo%2Fmerchandising&iid=M_99c4f712-7f6a-45df-bbc1-610638d8a878_1_372UD5BXDFYS_MC.VPTWYC0SXPYL&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Home%2B%2526%2BFurniture%7EBedroom%2BFurniture%7EBeds_VPTWYC0SXPYL&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all&cid=VPTWYC0SXPYL&page={}", 100, "bed")

# Read Excel files using pd.read_excel()
df_bed = pd.read_excel("E:/FINAL/bed.xlsx")

# Concatenate DataFrames
combined_df = pd.concat([df_bed], ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv("E:/FINAL/Combined_data_bed.csv", index=False)

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_lighting(base_url, page_no, dataframe_name):
    all_dataframes = []
    Product_Name = []
    Prices = []

    for i in range(2, page_no + 2):
        current_url = base_url.format(i)
        r = requests.get(current_url)
        soup = BeautifulSoup(r.text, "lxml")
        names = soup.find_all("a", class_="s1Q9rs")
        prices = soup.find_all("div", class_="_30jeq3")
        if r.status_code == 500:
            print(f"Internal Server Error (500) for {current_url}. Skipping this page.")
            continue
        for name, price in zip(names, prices):
            Product_Name.append(name.text)
            Prices.append(price.text)
# Rest of the code remains unchanged
        print(f"Length of Product_Name: {len(Product_Name)}")
        print(f"Length of Prices: {len(Prices)}")
    array_lengths = [len(Product_Name), len(Prices)]
    if len(set(array_lengths)) != 1:
        print(f"Arrays have inconsistent lengths. Skipping the creation of DataFrame.")
    else:
        df = pd.DataFrame({
            "Product Name": Product_Name,
            "Prices": Prices,
        })

    df['Prices'] = pd.to_numeric(df['Prices'].replace('[^\d.]', '', regex=True), errors='coerce')
    df = df.sort_values(by=['Prices'])

    all_dataframes.append(df)
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_excel(f"E:/FINAL/{dataframe_name}.xlsx", index=False)

# Example usage
scrape_flipkart_lighting("https://www.flipkart.com/home-lighting/decor-lighting-accessories/pr?sid=jhg%2C6w8&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_b661ec0e-9400-4b19-ac96-e37ab626d14a_1_372UD5BXDFYS_MC.NX0O0YGFEHU0&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Home%2B%2526%2BFurniture%7EHome%2BDecor%7ELightings_NX0O0YGFEHU0&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all&cid=NX0O0YGFEHU0&page={}", 1000, "lighting")

# Read Excel files using pd.read_excel()
df_lighting = pd.read_excel("E:/FINAL/lighting.xlsx")

# Concatenate DataFrames
combined_df = pd.concat([df_lighting], ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv("E:/FINAL/Combined_data_lighting.csv", index=False)


import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_printer(base_url, page_no, dataframe_name):
    all_dataframes = []
    Product_Name = []
    Prices = []

    for i in range(2, page_no + 2):
        current_url = base_url.format(i)
        r = requests.get(current_url)
        soup = BeautifulSoup(r.text, "lxml")
        names = soup.find_all("a", class_="s1Q9rs")
        prices = soup.find_all("div", class_="_30jeq3")
        if r.status_code == 500:
            print(f"Internal Server Error (500) for {current_url}. Skipping this page.")
            continue
        for name, price in zip(names, prices):
            Product_Name.append(name.text)
            Prices.append(price.text)
# Rest of the code remains unchanged
        print(f"Length of Product_Name: {len(Product_Name)}")
        print(f"Length of Prices: {len(Prices)}")
    array_lengths = [len(Product_Name), len(Prices)]
    if len(set(array_lengths)) != 1:
        print(f"Arrays have inconsistent lengths. Skipping the creation of DataFrame.")
    else:
        df = pd.DataFrame({
            "Product Name": Product_Name,
            "Prices": Prices,
        })

    df['Prices'] = pd.to_numeric(df['Prices'].replace('[^\d.]', '', regex=True), errors='coerce')
    df = df.sort_values(by=['Prices'])

    all_dataframes.append(df)
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_excel(f"E:/FINAL/{dataframe_name}.xlsx", index=False)

# Example usage
scrape_flipkart_printer("https://www.flipkart.com/computers/computer-peripherals/printers-inks/printers/pr?sid=6bo%2Ctia%2Cffn%2Ct64&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_889e2667-e71f-426a-9aa4-b542b3c640e6_1_372UD5BXDFYS_MC.ES1XN5J8PT49&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Electronics%7EComputer%2BPeripherals%7EPrinters_ES1XN5J8PT49&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all&cid=ES1XN5J8PT49&page={}", 100, "printer")

# Read Excel files using pd.read_excel()
df_printer = pd.read_excel("E:/FINAL/printer.xlsx")

# Concatenate DataFrames
combined_df = pd.concat([df_printer], ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv("E:/FINAL/Combined_data_printer.csv", index=False)


import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_trimmer(base_url, page_no, dataframe_name):
    all_dataframes = []
    Product_Name = []
    Prices = []

    for i in range(2, page_no + 2):
        current_url = base_url.format(i)
        r = requests.get(current_url)
        soup = BeautifulSoup(r.text, "lxml")
        names = soup.find_all("a", class_="s1Q9rs")
        prices = soup.find_all("div", class_="_30jeq3")
        if r.status_code == 500:
            print(f"Internal Server Error (500) for {current_url}. Skipping this page.")
            continue
        for name, price in zip(names, prices):
            Product_Name.append(name.text)
            Prices.append(price.text)
# Rest of the code remains unchanged
        print(f"Length of Product_Name: {len(Product_Name)}")
        print(f"Length of Prices: {len(Prices)}")
    array_lengths = [len(Product_Name), len(Prices)]
    if len(set(array_lengths)) != 1:
        print(f"Arrays have inconsistent lengths. Skipping the creation of DataFrame.")
    else:
        df = pd.DataFrame({
            "Product Name": Product_Name,
            "Prices": Prices,
        })

    df['Prices'] = pd.to_numeric(df['Prices'].replace('[^\d.]', '', regex=True), errors='coerce')
    df = df.sort_values(by=['Prices'])

    all_dataframes.append(df)
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_excel(f"E:/FINAL/{dataframe_name}.xlsx", index=False)

# Example usage
scrape_flipkart_trimmer("https://www.flipkart.com/health-personal-care-appliances/personal-care-appliances/trimmers/pr?sid=zlw%2C79s%2Cby3&fm=neo%2Fmerchandising&iid=M_3e048313-5f4e-4238-9ba9-57abe0d3571b_1_372UD5BXDFYS_MC.OFBY8SW4J77F&otracker=hp_rich_navigation_2_1.navigationCard.RICH_NAVIGATION_Electronics%7EHealth%2B%2526%2BPersonal%2BCare%7ETrimmers_OFBY8SW4J77F&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_2_L2_view-all&cid=OFBY8SW4J77F&page={}", 100, "trimmer")

# Read Excel files using pd.read_excel()
df_trimmer = pd.read_excel("E:/FINAL/trimmer.xlsx")

# Concatenate DataFrames
combined_df = pd.concat([df_trimmer], ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv("E:/FINAL/Combined_data_trimmer.csv", index=False)

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_homegym(base_url, page_no, dataframe_name):
    all_dataframes = []
    Product_Name = []
    Prices = []

    for i in range(2, page_no + 2):
        current_url = base_url.format(i)
        r = requests.get(current_url)
        soup = BeautifulSoup(r.text, "lxml")
        names = soup.find_all("a", class_="s1Q9rs")
        prices = soup.find_all("div", class_="_30jeq3")
        if r.status_code == 500:
            print(f"Internal Server Error (500) for {current_url}. Skipping this page.")
            continue
        for name, price in zip(names, prices):
            Product_Name.append(name.text)
            Prices.append(price.text)
# Rest of the code remains unchanged
        print(f"Length of Product_Name: {len(Product_Name)}")
        print(f"Length of Prices: {len(Prices)}")
    array_lengths = [len(Product_Name), len(Prices)]
    if len(set(array_lengths)) != 1:
        print(f"Arrays have inconsistent lengths. Skipping the creation of DataFrame.")
    else:
        df = pd.DataFrame({
            "Product Name": Product_Name,
            "Prices": Prices,
        })

    df['Prices'] = pd.to_numeric(df['Prices'].replace('[^\d.]', '', regex=True), errors='coerce')
    df = df.sort_values(by=['Prices'])

    all_dataframes.append(df)
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_excel(f"E:/FINAL/{dataframe_name}.xlsx", index=False)

# Example usage
scrape_flipkart_homegym("https://www.flipkart.com/exercise-fitness/fitness-equipments/fitness-kits/pr?sid=qoc%2Camf%2Cvh3&p%5B%5D=facets.serviceability%5B%5D%3Dtrue&otracker=categorytree&otracker=nmenu_sub_Sports%2C+Books+%26+More_0_Home+Gyms&page={}", 100, "homegym")

# Read Excel files using pd.read_excel()
df_homegym = pd.read_excel("E:/FINAL/homegym.xlsx")

# Concatenate DataFrames
combined_df = pd.concat([df_homegym], ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv("E:/FINAL/Combined_data_homegym.csv", index=False)

import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_silverjewel(base_url, page_no, dataframe_name):
    all_dataframes = []
    Product_Name = []
    Prices = []

    for i in range(2, page_no + 2):
        current_url = base_url.format(i)
        r = requests.get(current_url)
        soup = BeautifulSoup(r.text, "lxml")
        names = soup.find_all("div", class_="_2WkVRV")
        prices = soup.find_all("div", class_="_30jeq3")
        if r.status_code == 500:
            print(f"Internal Server Error (500) for {current_url}. Skipping this page.")
            continue
        for name, price in zip(names, prices):
            Product_Name.append(name.text)
            Prices.append(price.text)
# Rest of the code remains unchanged
        print(f"Length of Product_Name: {len(Product_Name)}")
        print(f"Length of Prices: {len(Prices)}")
    array_lengths = [len(Product_Name), len(Prices)]
    if len(set(array_lengths)) != 1:
        print(f"Arrays have inconsistent lengths. Skipping the creation of DataFrame.")
    else:
        df = pd.DataFrame({
            "Product Name": Product_Name,
            "Prices": Prices,
        })

    df['Prices'] = pd.to_numeric(df['Prices'].replace('[^\d.]', '', regex=True), errors='coerce')
    df = df.sort_values(by=['Prices'])

    all_dataframes.append(df)
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_excel(f"E:/FINAL/{dataframe_name}.xlsx", index=False)

# Example usage
scrape_flipkart_silverjewel("https://flipkart.com/jewellery/silver-jewellery/pr?sid=mcr%2Ctfz&otracker=nmenu_sub_Women_0_Silver+Jewellery&page={}", 1000, "silverjewel")

# Read Excel files using pd.read_excel()
df_silverjewel = pd.read_excel("E:/FINAL/silverjewel.xlsx")

# Concatenate DataFrames
combined_df = pd.concat([df_silverjewel], ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv("E:/FINAL/Combined_data_silverjewel.csv", index=False)


import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_flipkart_two_wheeler(base_url, page_no, dataframe_name):
    all_dataframes = []
    Product_Name = []
    Prices = []
    Maximum_Power= []
    Displacement = []
    Brake_Front = []
    Console_feature = []

    for i in range(2, page_no + 2):
        current_url = base_url.format(i)
        r = requests.get(current_url)
        soup = BeautifulSoup(r.text, "lxml")

        names = soup.find_all("div", class_="_4rR01T")
        prices = soup.find_all("div", class_="_30jeq3 _1_WHN1")
        descriptions = soup.find_all("div", class_="fMghEO")
        
        if r.status_code == 500:
            print(f"Internal Server Error (500) for {current_url}. Skipping this page.")
            continue

        for name, price, description in zip(names, prices, descriptions):
            Product_Name.append(name.text)
            Prices.append(price.text)
            Maximum_Power.append(description.find("li", string=lambda s: "Maximum Speed" in s).text.strip() if description.find("li", string=lambda s: "Maximum Speed" in s) else "")
            Displacement.append(description.find("li", string=lambda s: "Displacement" in s).text.strip() if description.find("li", string=lambda s: "Displacement" in s) else "")
            Brake_Front.append(description.find("li", string=lambda s: "Brake front" in s).text.strip() if description.find("li", string=lambda s: "Brake front" in s) else "")
            Console_feature.append(description.find("li", string=lambda s: "Console Feature" in s).text.strip() if description.find("li", string=lambda s: "Console Feature" in s) else "")
          # Add this before creating the DataFrame
        print(f"Length of Product_Name: {len(Product_Name)}")
        print(f"Length of Prices: {len(Prices)}")
        print(f"Length of Maximum Speed: {len(Maximum_Power)}")
        print(f"Length of Displacement: {len(Displacement)}")
        print(f"Length of Brake front: {len(Brake_Front)}")
        print(f"Length of Console Feature: {len(Console_feature)}")
    # Check if all arrays have the same length
    array_lengths = [len(Product_Name), len(Prices), len(Maximum_Power), len(Displacement), len(Brake_Front), len(Console_feature)]
    if len(set(array_lengths)) != 1:
        print(f"Arrays have inconsistent lengths. Skipping the creation of DataFrame.")
    else:
        df = pd.DataFrame({
            "Product Name": Product_Name,
            "Prices": Prices,
            "Maximum Speed": Maximum_Power,
            "Displacement": Displacement,
            "Brake front": Brake_Front,
            "Console Feature": Console_feature
        })

    df['Prices'] = pd.to_numeric(df['Prices'].replace('[^\d.]', '', regex=True), errors='coerce')
    df = df.sort_values(by=['Prices'])

    all_dataframes.append(df)
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_excel(f"E:/FINAL/{dataframe_name}.xlsx", index=False)

# Example usage
scrape_flipkart_two_wheeler("https://www.flipkart.com/search?q=two+wheeler+bike&sid=7dk%2C0aj&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&as-pos=1&as-type=RECENT&suggestionId=two+wheeler+bike%7CBikes+%26+Scooters&requestId=580c14f1-16b5-445f-a64e-29a9e1967940&as-searchtext=two+wh&page={}", 400, "two_wheeler")


# Read Excel files using pd.read_excel()
df_i_two_wheeler = pd.read_excel("E:/FINAL/two_wheeler.xlsx")




# Concatenate DataFrames
combined_df = pd.concat([df_i_two_wheeler], ignore_index=True)

# Save the combined DataFrame to a CSV file
combined_df.to_csv("E:/FINAL/Combined_data_two_wheeler.csv", index=False)