import csv

# 학생 데이터를 파일에서 읽어오는 함수
def load_data(file_name):
    data = []
    try:
        with open(file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"{file_name} not found. Starting with an empty dataset.")
        # 초기 데이터 추가
        data = [
    ["7-1", "7101", "고*진", "0"],
    ["7-1", "7102", "김*율", "0"],
    ["7-1", "7103", "김*희", "0"],
    ["7-1", "7104", "김*림", "0"],
    ["7-1", "7105", "김*민", "0"],
    ["7-1", "7106", "김*윤", "0"],
    ["7-1", "7107", "문*우", "0"],
    ["7-1", "7108", "박*연", "0"],
    ["7-1", "7109", "박*빈", "0"],
    ["7-1", "7110", "박*은", "0"],
    ["7-1", "7111", "박*이", "0"],
    ["7-1", "7112", "박*아", "0"],
    ["7-1", "7113", "박*경", "0"],
    ["7-1", "7114", "박*밀", "0"],
    ["7-1", "7115", "손*현", "0"],
    ["7-1", "7116", "신*원", "0"],
    ["7-1", "7117", "안*우", "0"],
    ["7-1", "7118", "엄*비", "0"],
    ["7-1", "7119", "윤*원", "0"],
    ["7-1", "7120", "이*민", "0"],
    ["7-1", "7121", "이*현", "0"],
    ["7-1", "7122", "이*원", "0"],
    ["7-1", "7123", "임*현", "0"],
    ["7-1", "7124", "장*성", "0"],
    ["7-1", "7125", "전*아", "0"],
    ["7-1", "7126", "정*홍", "0"],
    ["7-1", "7127", "정*우", "0"],
    ["7-1", "7128", "정*찬", "0"],
    ["7-1", "7129", "조*하", "0"],
    ["7-1", "7130", "최*영", "0"],
    ["7-1", "7131", "최*원", "0"],
    ["7-1", "7132", "한*리", "0"],
    ["7-1", "7133", "한*찬", "0"],
    ["7-1", "7134", "허*현", "0"],
    ["7-2", "7201", "구*건", "0"],
    ["7-2", "7202", "권*혁", "0"],
    ["7-2", "7203", "김*리", "0"],
    ["7-2", "7204", "김*모", "0"],
    ["7-2", "7205", "김*언", "0"],
    ["7-2", "7206", "김*민", "0"],
    ["7-2", "7207", "김*나", "0"],
    ["7-2", "7208", "김*아", "0"],
    ["7-2", "7209", "박*호", "0"],
    ["7-2", "7210", "박*윤", "0"],
    ["7-2", "7211", "박*한", "0"],
    ["7-2", "7212", "박*성", "0"],
    ["7-2", "7213", "박*우", "0"],
    ["7-2", "7214", "박*효", "0"],
    ["7-2", "7215", "박*규", "0"],
    ["7-2", "7216", "성*미", "0"],
    ["7-2", "7217", "손*완", "0"],
    ["7-2", "7218", "안*혁", "0"],
    ["7-2", "7219", "유*연", "0"],
    ["7-2", "7220", "유*림", "0"],
    ["7-2", "7221", "이*은", "0"],
    ["7-2", "7222", "이*준", "0"],
    ["7-2", "7223", "이*은", "0"],
    ["7-2", "7224", "이*민", "0"],
    ["7-2", "7225", "이*원", "0"],
    ["7-2", "7226", "임*영", "0"],
    ["7-2", "7227", "정*윤", "0"],
    ["7-2", "7228", "정*경", "0"],
    ["7-2", "7229", "정*진", "0"],
    ["7-2", "7230", "조*빈", "0"],
    ["7-2", "7231", "조*설", "0"],
    ["7-2", "7232", "진*원", "0"],
    ["7-2", "7233", "진*영", "0"],
    ["7-2", "7234", "천*영", "0"],
    ["7-2", "7235", "최*규", "0"],
    ["7-3", "7301", "강*현", "0"],
    ["7-3", "7302", "강*후", "0"],
    ["7-3", "7303", "강*민", "0"],
    ["7-3", "7304", "강*원", "0"],
    ["7-3", "7305", "고*솔", "0"],
    ["7-3", "7306", "김*현", "0"],
    ["7-3", "7307", "김*준", "0"],
    ["7-3", "7308", "김*연", "0"],
    ["7-3", "7309", "김*겸", "0"],
    ["7-3", "7310", "김*준", "0"],
    ["7-3", "7311", "김*환", "0"],
    ["7-3", "7312", "김*준", "0"],
    ["7-3", "7313", "박*온", "0"],
    ["7-3", "7314", "박*우", "0"],
    ["7-3", "7315", "백*인", "0"],
    ["7-3", "7316", "사*주", "0"],
    ["7-3", "7317", "송*훈", "0"],
    ["7-3", "7318", "유*환", "0"],
    ["7-3", "7319", "윤*영", "0"],
    ["7-3", "7320", "이*비", "0"],
    ["7-3", "7321", "이*재", "0"],
    ["7-3", "7322", "이*수", "0"],
    ["7-3", "7323", "임*연", "0"],
    ["7-3", "7324", "장*준", "0"],
    ["7-3", "7325", "장*기", "0"],
    ["7-3", "7326", "장*은", "0"],
    ["7-3", "7327", "정*윤", "0"],
    ["7-3", "7328", "조*하", "0"],
    ["7-3", "7329", "지*수아", "0"],
    ["7-3", "7330", "함*빈", "0"],
    ["7-3", "7331", "홍*이", "0"],
    ["7-3", "7332", "홍*아", "0"],
    ["7-3", "7333", "황*아", "0"],
    ["7-3", "7334", "황*수", "0"],
    ["7-4", "7401", "강*정", "0"],
    ["7-4", "7402", "김*성", "0"],
    ["7-4", "7403", "김*민", "0"],
    ["7-4", "7404", "박*연", "0"],
    ["7-4", "7405", "박*연", "0"],
    ["7-4", "7406", "박*라", "0"],
    ["7-4", "7407", "박*하", "0"],
    ["7-4", "7408", "박*수", "0"],
    ["7-4", "7409", "박*나", "0"],
    ["7-4", "7410", "방*서", "0"],
    ["7-4", "7411", "백*지", "0"],
    ["7-4", "7412", "서*준", "0"],
    ["7-4", "7413", "신*윤", "0"],
    ["7-4", "7414", "양*희", "0"],
    ["7-4", "7415", "이*빈", "0"],
    ["7-4", "7416", "이*아", "0"],
    ["7-4", "7417", "이*은", "0"],
    ["7-4", "7418", "이*마", "0"],
    ["7-4", "7419", "이*호", "0"],
    ["7-4", "7420", "이*희", "0"],
    ["7-4", "7421", "이*규", "0"],
    ["7-4", "7422", "전*환", "0"],
    ["7-4", "7423", "전*찬", "0"],
    ["7-4", "7424", "전*원", "0"],
    ["7-4", "7425", "정*권", "0"],
    ["7-4", "7426", "정*정", "0"],
    ["7-4", "7427", "정*연", "0"],
    ["7-4", "7428", "정*우", "0"],
    ["7-4", "7429", "정*윤", "0"],
    ["7-4", "7430", "조*부", "0"],
    ["7-4", "7431", "차*나", "0"],
    ["7-4", "7432", "최*진", "0"],
    ["7-4", "7433", "홍*기", "0"],
    ["7-5", "7501", "강*나", "0"],
    ["7-5", "7502", "고*재", "0"],
    ["7-5", "7503", "고*우", "0"],
    ["7-5", "7504", "구*민", "0"],
    ["7-5", "7505", "권*미나", "0"],
    ["7-5", "7506", "김*영", "0"],
    ["7-5", "7507", "김*준", "0"],
    ["7-5", "7508", "김*희", "0"],
    ["7-5", "7509", "김*민", "0"],
    ["7-5", "7510", "김*서", "0"],
    ["7-5", "7511", "김*아", "0"],
    ["7-5", "7512", "김*림", "0"],
    ["7-5", "7513", "김*서", "0"],
    ["7-5", "7514", "김*현", "0"],
    ["7-5", "7515", "김*호", "0"],
    ["7-5", "7516", "김*율", "0"],
    ["7-5", "7517", "나*리", "0"],
    ["7-5", "7518", "마*정", "0"],
    ["7-5", "7519", "박*현", "0"],
    ["7-5", "7520", "박*민", "0"],
    ["7-5", "7521", "백*우", "0"],
    ["7-5", "7522", "송*은", "0"],
    ["7-5", "7523", "송*서", "0"],
    ["7-5", "7524", "이*우", "0"],
    ["7-5", "7525", "이*서", "0"],
    ["7-5", "7526", "이*우", "0"],
    ["7-5", "7527", "장*원", "0"],
    ["7-5", "7528", "조*진", "0"],
    ["7-5", "7529", "조*영", "0"],
    ["7-5", "7530", "주*희", "0"],
    ["7-5", "7531", "주*광", "0"],
    ["7-5", "7532", "한*윤", "0"],
    ["7-5", "7533", "황*인", "0"],
    ["7-5", "7534", "황*연", "0"],
    ["8-1", "8101", "고*군", "0"],
    ["8-1", "8102", "김*구", "0"],
    ["8-1", "8103", "김*연", "0"],
    ["8-1", "8104", "김*성", "0"],
    ["8-1", "8105", "김*준", "0"],
    ["8-1", "8106", "김*용", "0"],
    ["8-1", "8107", "김*안", "0"],
    ["8-1", "8108", "박*유", "0"],
    ["8-1", "8109", "박*민", "0"],
    ["8-1", "8110", "박*아", "0"],
    ["8-1", "8111", "박*나", "0"],
    ["8-1", "8112", "박*준", "0"],
    ["8-1", "8113", "백*민", "0"],
    ["8-1", "8114", "신*희", "0"],
    ["8-1", "8115", "안*유", "0"],
    ["8-1", "8116", "오*은", "0"],
    ["8-1", "8117", "오*유", "0"],
    ["8-1", "8118", "우*우", "0"],
    ["8-1", "8119", "이*진", "0"],
    ["8-1", "8120", "이*헌", "0"],
    ["8-1", "8121", "이*범", "0"],
    ["8-1", "8122", "이*민", "0"],
    ["8-1", "8123", "임*호", "0"],
    ["8-1", "8124", "임*웅", "0"],
    ["8-1", "8125", "장*우", "0"],
    ["8-1", "8126", "정*미", "0"],
    ["8-1", "8127", "조*우", "0"],
    ["8-1", "8128", "조*경", "0"],
    ["8-1", "8129", "주*민", "0"],
    ["8-1", "8130", "최*기", "0"],
    ["8-1", "8131", "최*망", "0"],
    ["8-1", "8132", "최*윤", "0"],
    ["8-1", "8133", "최*웅", "0"],
    ["8-1", "8134", "홍*진", "0"],
    ["8-2", "8201", "강*준", "0"],
    ["8-2", "8202", "고*형", "0"],
    ["8-2", "8203", "국*영", "0"],
    ["8-2", "8204", "김*윤", "0"],
    ["8-2", "8205", "김*우", "0"],
    ["8-2", "8206", "김*구", "0"],
    ["8-2", "8207", "김*준", "0"],
    ["8-2", "8208", "김*", "0"],
    ["8-2", "8209", "김*연", "0"],
    ["8-2", "8210", "김*준", "0"],
    ["8-2", "8211", "김*인", "0"],
    ["8-2", "8212", "노*서", "0"],
    ["8-2", "8213", "박*현", "0"],
    ["8-2", "8214", "박*아", "0"],
    ["8-2", "8215", "박*기", "0"],
    ["8-2", "8216", "손*안", "0"],
    ["8-2", "8217", "신*린", "0"],
    ["8-2", "8218", "이*영", "0"],
    ["8-2", "8219", "이*빈", "0"],
    ["8-2", "8220", "이*형", "0"],
    ["8-2", "8221", "이*나", "0"],
    ["8-2", "8222", "이*후", "0"],
    ["8-2", "8223", "임*율", "0"],
    ["8-2", "8224", "장*혁", "0"],
    ["8-2", "8225", "전*은", "0"],
    ["8-2", "8226", "정*서", "0"],
    ["8-2", "8227", "정*빈", "0"],
    ["8-2", "8228", "정*원", "0"],
    ["8-2", "8229", "지*나", "0"],
    ["8-2", "8230", "최*수", "0"],
    ["8-2", "8231", "편*아", "0"],
    ["8-2", "8232", "하*율", "0"],
    ["8-2", "8233", "한*원", "0"],
    ["8-2", "8234", "홍*민", "0"],
    ["8-3", "8301", "강*하", "0"],
    ["8-3", "8302", "권*진", "0"],
    ["8-3", "8303", "김*연", "0"],
    ["8-3", "8304", "김*윤", "0"],
    ["8-3", "8305", "김*경", "0"],
    ["8-3", "8306", "김*중", "0"],
    ["8-3", "8307", "김*주", "0"],
    ["8-3", "8308", "김*수", "0"],
    ["8-3", "8309", "김*지", "0"],
    ["8-3", "8310", "김*나", "0"],
    ["8-3", "8311", "나*정", "0"],
    ["8-3", "8312", "명*율", "0"],
    ["8-3", "8313", "백*진", "0"],
    ["8-3", "8314", "손*인", "0"],
    ["8-3", "8315", "송*아", "0"],
    ["8-3", "8316", "송*민", "0"],
    ["8-3", "8317", "신*철", "0"],
    ["8-3", "8318", "안*준", "0"],
    ["8-3", "8319", "안*미", "0"],
    ["8-3", "8320", "양*준", "0"],
    ["8-3", "8321", "오*온", "0"],
    ["8-3", "8322", "이*규", "0"],
    ["8-3", "8323", "이*아", "0"],
    ["8-3", "8324", "이*민", "0"],
    ["8-3", "8325", "이*영", "0"],
    ["8-3", "8326", "임*온", "0"],
    ["8-3", "8327", "임*서", "0"],
    ["8-3", "8328", "장*석", "0"],
    ["8-3", "8329", "정*규", "0"],
    ["8-3", "8330", "정*우", "0"],
    ["8-3", "8331", "정*준", "0"],
    ["8-3", "8332", "추*미", "0"],
    ["8-3", "8333", "황*욱", "0"],
    ["8-4", "8401", "강*완", "0"],
    ["8-4", "8402", "구*준", "0"],
    ["8-4", "8403", "권*혁", "0"],
    ["8-4", "8404", "길*서", "0"],
    ["8-4", "8405", "김*중", "0"],
    ["8-4", "8406", "김*재", "0"],
    ["8-4", "8407", "김*율", "0"],
    ["8-4", "8408", "김*윤", "0"],
    ["8-4", "8409", "김*빈", "0"],
    ["8-4", "8410", "남*민", "0"],
    ["8-4", "8411", "민*니엘", "0"],
    ["8-4", "8412", "민*현", "0"],
    ["8-4", "8413", "박*찬", "0"],
    ["8-4", "8414", "박*현", "0"],
    ["8-4", "8415", "박*민", "0"],
    ["8-4", "8416", "박*하", "0"],
    ["8-4", "8417", "박*영", "0"],
    ["8-4", "8418", "백*주", "0"],
    ["8-4", "8419", "백*림", "0"],
    ["8-4", "8420", "서*", "0"],
    ["8-4", "8421", "손*주", "0"],
    ["8-4", "8422", "신*철", "0"],
    ["8-4", "8423", "안*윤", "0"],
    ["8-4", "8424", "어*민", "0"],
    ["8-4", "8425", "유*호", "0"],
    ["8-4", "8426", "이*아", "0"],
    ["8-4", "8427", "이*연", "0"],
    ["8-4", "8428", "이*민", "0"],
    ["8-4", "8429", "정*아", "0"],
    ["8-4", "8430", "주*하", "0"],
    ["8-4", "8431", "차*유", "0"],
    ["8-4", "8432", "차*호", "0"],
    ["8-4", "8433", "한*란", "0"],
    ["8-5", "8501", "강*재", "0"],
    ["8-5", "8502", "고*서", "0"],
    ["8-5", "8503", "권*현", "0"],
    ["8-5", "8504", "김*권", "0"],
    ["8-5", "8505", "김*명", "0"],
    ["8-5", "8506", "김*영", "0"],
    ["8-5", "8507", "김*헌", "0"],
    ["8-5", "8508", "나*리", "0"],
    ["8-5", "8509", "나*겸", "0"],
    ["8-5", "8510", "남*훈", "0"],
    ["8-5", "8511", "노*윤", "0"],
    ["8-5", "8512", "문*은", "0"],
    ["8-5", "8513", "박*리", "0"],
    ["8-5", "8514", "박*근", "0"],
    ["8-5", "8515", "박*민", "0"],
    ["8-5", "8516", "박*우", "0"],
    ["8-5", "8517", "박*수", "0"],
    ["8-5", "8518", "박*준", "0"],
    ["8-5", "8519", "서*아", "0"],
    ["8-5", "8520", "신*호", "0"],
    ["8-5", "8521", "오*우", "0"],
    ["8-5", "8522", "윤*영", "0"],
    ["8-5", "8523", "윤*영", "0"],
    ["8-5", "8524", "이*린", "0"],
    ["8-5", "8525", "이*성", "0"],
    ["8-5", "8526", "이*후", "0"],
    ["8-5", "8527", "이*욱", "0"],
    ["8-5", "8528", "이*남", "0"],
    ["8-5", "8529", "정*윤", "0"],
    ["8-5", "8530", "정*우", "0"],
    ["8-5", "8531", "정*원", "0"],
    ["8-5", "8532", "주*서", "0"],
    ["8-5", "8533", "최*결", "0"],
    ["8-5", "8534", "한*웅", "0"],
    ["9-1", "9101", "강*율", "0"],
    ["9-1", "9102", "강*윤", "0"],
    ["9-1", "9103", "강*인", "0"],
    ["9-1", "9104", "고*우", "0"],
    ["9-1", "9105", "곽*기", "0"],
    ["9-1", "9106", "구*정", "0"],
    ["9-1", "9107", "김*라", "0"],
    ["9-1", "9108", "김*", "0"],
    ["9-1", "9109", "김*민", "0"],
    ["9-1", "9110", "김*성", "0"],
    ["9-1", "9111", "김*서", "0"],
    ["9-1", "9112", "박*빈", "0"],
    ["9-1", "9113", "박*온", "0"],
    ["9-1", "9114", "박*수", "0"],
    ["9-1", "9115", "박*연", "0"],
    ["9-1", "9116", "백*린", "0"],
    ["9-1", "9117", "서*서", "0"],
    ["9-1", "9118", "선*아", "0"],
    ["9-1", "9119", "신*희", "0"],
    ["9-1", "9120", "유*인", "0"],
    ["9-1", "9121", "윤*현", "0"],
    ["9-1", "9122", "이*빈", "0"],
    ["9-1", "9123", "이*율", "0"],
    ["9-1", "9124", "이*민", "0"],
    ["9-1", "9125", "이*유", "0"],
    ["9-1", "9126", "이*리", "0"],
    ["9-1", "9127", "정*진", "0"],
    ["9-1", "9128", "정*민", "0"],
    ["9-1", "9129", "진*우", "0"],
    ["9-1", "9130", "최*원", "0"],
    ["9-1", "9131", "홍*", "0"],
    ["9-1", "9132", "황*연", "0"],
    ["9-1", "9133", "황*서", "0"],
    ["9-2", "9201", "강*재", "0"],
    ["9-2", "9202", "강*석", "0"],
    ["9-2", "9203", "강*후", "0"],
    ["9-2", "9204", "강*나", "0"],
    ["9-2", "9205", "고*우", "0"],
    ["9-2", "9206", "구*명", "0"],
    ["9-2", "9207", "김*준", "0"],
    ["9-2", "9208", "김*화", "0"],
    ["9-2", "9209", "김*진", "0"],
    ["9-2", "9210", "김*영", "0"],
    ["9-2", "9211", "김*은", "0"],
    ["9-2", "9212", "김*서", "0"],
    ["9-2", "9213", "김*린", "0"],
    ["9-2", "9214", "김*원", "0"],
    ["9-2", "9215", "문*민", "0"],
    ["9-2", "9216", "민*홍", "0"],
    ["9-2", "9217", "박*상", "0"],
    ["9-2", "9218", "손*민", "0"],
    ["9-2", "9219", "손*준", "0"],
    ["9-2", "9220", "오*령", "0"],
    ["9-2", "9221", "이*규", "0"],
    ["9-2", "9222", "이*진", "0"],
    ["9-2", "9223", "이*경", "0"],
    ["9-2", "9224", "이*서", "0"],
    ["9-2", "9225", "정*우", "0"],
    ["9-2", "9226", "조*영", "0"],
    ["9-2", "9227", "최*명", "0"],
    ["9-2", "9228", "최*석", "0"],
    ["9-2", "9229", "한*라", "0"],
    ["9-2", "9230", "한*서", "0"],
    ["9-2", "9231", "한*진", "0"],
    ["9-2", "9232", "홍*민", "0"],
    ["9-2", "9233", "황*하", "0"],
    ["9-3", "9301", "구*훈", "0"],
    ["9-3", "9302", "김*리", "0"],
    ["9-3", "9303", "김*준", "0"],
    ["9-3", "9304", "김*채", "0"],
    ["9-3", "9305", "김*현", "0"],
    ["9-3", "9306", "김*인", "0"],
    ["9-3", "9307", "김*현", "0"],
    ["9-3", "9308", "김*우", "0"],
    ["9-3", "9309", "김*윤", "0"],
    ["9-3", "9310", "박*민", "0"],
    ["9-3", "9311", "박*현", "0"],
    ["9-3", "9312", "박*현", "0"],
    ["9-3", "9313", "박*우", "0"],
    ["9-3", "9314", "박*진", "0"],
    ["9-3", "9315", "박*수", "0"],
    ["9-3", "9316", "백*라", "0"],
    ["9-3", "9317", "신*진", "0"],
    ["9-3", "9318", "안*중", "0"],
    ["9-3", "9319", "오*욱", "0"],
    ["9-3", "9320", "오*원", "0"],
    ["9-3", "9321", "유*", "0"],
    ["9-3", "9322", "윤*아", "0"],
    ["9-3", "9323", "윤*언", "0"],
    ["9-3", "9324", "이*원", "0"],
    ["9-3", "9325", "이*서", "0"],
    ["9-3", "9326", "이*진", "0"],
    ["9-3", "9327", "이*주", "0"],
    ["9-3", "9328", "장*기", "0"],
    ["9-3", "9329", "정*진", "0"],
    ["9-3", "9330", "정*우", "0"],
    ["9-3", "9331", "조*철", "0"],
    ["9-3", "9332", "차*빈", "0"],
    ["9-3", "9333", "천*현", "0"],
    ["9-4", "9401", "강*영", "0"],
    ["9-4", "9402", "강*서", "0"],
    ["9-4", "9403", "권*철", "0"],
    ["9-4", "9404", "김*우", "0"],
    ["9-4", "9405", "김*하", "0"],
    ["9-4", "9406", "김*경", "0"],
    ["9-4", "9407", "김*린", "0"],
    ["9-4", "9408", "김*석", "0"],
    ["9-4", "9409", "김*후", "0"],
    ["9-4", "9410", "김*준", "0"],
    ["9-4", "9411", "라*명", "0"],
    ["9-4", "9412", "류*훈", "0"],
    ["9-4", "9413", "민*영", "0"],
    ["9-4", "9414", "박*준", "0"],
    ["9-4", "9415", "박*온", "0"],
    ["9-4", "9416", "박*담", "0"],
    ["9-4", "9417", "배*서", "0"],
    ["9-4", "9418", "변*린", "0"],
    ["9-4", "9419", "손*연", "0"],
    ["9-4", "9420", "송*희", "0"],
    ["9-4", "9421", "이*나", "0"],
    ["9-4", "9422", "이*주", "0"],
    ["9-4", "9423", "임*온", "0"],
    ["9-4", "9424", "임*민", "0"],
    ["9-4", "9425", "장*인", "0"],
    ["9-4", "9426", "정*진", "0"],
    ["9-4", "9427", "조*림", "0"],
    ["9-4", "9428", "최*우", "0"],
    ["9-4", "9429", "추*미", "0"],
    ["9-4", "9430", "하*린", "0"],
    ["9-4", "9431", "현*연", "0"],
    ["9-4", "9432", "홍*민", "0"],
    ["9-4", "9433", "황*환", "0"],
    ["9-5", "9501", "강*재", "0"],
    ["9-5", "9502", "곽*하", "0"],
    ["9-5", "9503", "김*진", "0"],
    ["9-5", "9504", "김*민", "0"],
    ["9-5", "9505", "김*성", "0"],
    ["9-5", "9506", "김*승", "0"],
    ["9-5", "9507", "김*원", "0"],
    ["9-5", "9508", "김*우", "0"],
    ["9-5", "9509", "나*빈", "0"],
    ["9-5", "9510", "도*림", "0"],
    ["9-5", "9511", "문*민", "0"],
    ["9-5", "9512", "문*찬", "0"],
    ["9-5", "9513", "박*준", "0"],
    ["9-5", "9514", "박*윤", "0"],
    ["9-5", "9515", "반*영", "0"],
    ["9-5", "9516", "배*주", "0"],
    ["9-5", "9517", "심*진", "0"],
    ["9-5", "9518", "안*연", "0"],
    ["9-5", "9519", "양*민", "0"],
    ["9-5", "9520", "오*호", "0"],
    ["9-5", "9521", "오*헌", "0"],
    ["9-5", "9522", "오*영", "0"],
    ["9-5", "9523", "유*수", "0"],
    ["9-5", "9524", "이*은", "0"],
    ["9-5", "9525", "이*남", "0"],
    ["9-5", "9526", "장*수", "0"],
    ["9-5", "9527", "장*나", "0"],
    ["9-5", "9528", "전*준", "0"],
    ["9-5", "9529", "전*현", "0"],
    ["9-5", "9530", "채*은", "0"],
    ["9-5", "9531", "최*우", "0"],
    ["9-5", "9532", "홍*나", "0"],
    ["9-5", "9533", "황*준", "0"],
    ["10-1", "10101", "고*선", "0"],
    ["10-1", "10102", "권*안나", "0"],
    ["10-1", "10103", "김*이", "0"],
    ["10-1", "10104", "김*준", "0"],
    ["10-1", "10105", "김*안", "0"],
    ["10-1", "10106", "김*우", "0"],
    ["10-1", "10107", "김*필", "0"],
    ["10-1", "10108", "김*수", "0"],
    ["10-1", "10109", "남*우", "0"],
    ["10-1", "10110", "노*민", "0"],
    ["10-1", "10111", "류*", "0"],
    ["10-1", "10112", "민*기", "0"],
    ["10-1", "10113", "박*을", "0"],
    ["10-1", "10114", "박*한", "0"],
    ["10-1", "10115", "박*오", "0"],
    ["10-1", "10116", "박*율", "0"],
    ["10-1", "10117", "성*후", "0"],
    ["10-1", "10118", "신*민", "0"],
    ["10-1", "10119", "양*우", "0"],
    ["10-1", "10120", "양*웅", "0"],
    ["10-1", "10121", "오*윤", "0"],
    ["10-1", "10122", "우*지", "0"],
    ["10-1", "10123", "이*라", "0"],
    ["10-1", "10124", "이*우", "0"],
    ["10-1", "10125", "이*서", "0"],
    ["10-1", "10126", "이*원", "0"],
    ["10-1", "10127", "이*주", "0"],
    ["10-1", "10128", "정*아", "0"],
    ["10-1", "10129", "조*제", "0"],
    ["10-1", "10130", "조*성", "0"],
    ["10-1", "10131", "조*서", "0"],
    ["10-1", "10132", "최*혜", "0"],
    ["10-1", "10133", "황*담", "0"],
    ["10-2", "10201", "강*은", "0"],
    ["10-2", "10202", "고*빈", "0"],
    ["10-2", "10203", "권*종", "0"],
    ["10-2", "10204", "김*경", "0"],
    ["10-2", "10205", "김*영", "0"],
    ["10-2", "10206", "김*준", "0"],
    ["10-2", "10207", "김*하", "0"],
    ["10-2", "10208", "김*희", "0"],
    ["10-2", "10209", "김*호", "0"],
    ["10-2", "10210", "김*환", "0"],
    ["10-2", "10211", "김*준", "0"],
    ["10-2", "10212", "김*겸", "0"],
    ["10-2", "10213", "노*진", "0"],
    ["10-2", "10214", "민*인", "0"],
    ["10-2", "10215", "박*영", "0"],
    ["10-2", "10216", "박*영", "0"],
    ["10-2", "10217", "박*수", "0"],
    ["10-2", "10218", "방*이", "0"],
    ["10-2", "10219", "배*진", "0"],
    ["10-2", "10220", "배*호", "0"],
    ["10-2", "10221", "서*원", "0"],
    ["10-2", "10222", "서*강", "0"],
    ["10-2", "10223", "손*원", "0"],
    ["10-2", "10224", "신*영", "0"],
    ["10-2", "10225", "안*후", "0"],
    ["10-2", "10226", "어*민", "0"],
    ["10-2", "10227", "오*나", "0"],
    ["10-2", "10228", "윤*아", "0"],
    ["10-2", "10229", "정*교", "0"],
    ["10-2", "10230", "정*원", "0"],
    ["10-2", "10231", "정*서", "0"],
    ["10-2", "10232", "채*림", "0"],
    ["10-2", "10233", "최*석", "0"],
    ["10-2", "10234", "황*나", "0"],
    ["10-3", "10301", "고*근", "0"],
    ["10-3", "10302", "공*윤", "0"],
    ["10-3", "10303", "김*윤", "0"],
    ["10-3", "10304", "김*선", "0"],
    ["10-3", "10305", "김*찬", "0"],
    ["10-3", "10306", "김*유", "0"],
    ["10-3", "10307", "김*원", "0"],
    ["10-3", "10308", "김*람", "0"],
    ["10-3", "10309", "김*건", "0"],
    ["10-3", "10310", "노*빈", "0"],
    ["10-3", "10311", "문*늘", "0"],
    ["10-3", "10312", "민*윤", "0"],
    ["10-3", "10313", "박*창", "0"],
    ["10-3", "10314", "박*호", "0"],
    ["10-3", "10315", "박*한", "0"],
    ["10-3", "10316", "박*은", "0"],
    ["10-3", "10317", "박*겸", "0"],
    ["10-3", "10318", "서*현", "0"],
    ["10-3", "10319", "송*윤", "0"],
    ["10-3", "10320", "안*현", "0"],
    ["10-3", "10321", "오*원", "0"],
    ["10-3", "10322", "이*준", "0"],
    ["10-3", "10323", "이*정", "0"],
    ["10-3", "10324", "이*후", "0"],
    ["10-3", "10325", "이*림", "0"],
    ["10-3", "10326", "임*은", "0"],
    ["10-3", "10327", "임*민", "0"],
    ["10-3", "10328", "정*치", "0"],
    ["10-3", "10329", "정*우", "0"],
    ["10-3", "10330", "조*진", "0"],
    ["10-3", "10331", "지*원", "0"],
    ["10-3", "10332", "하*정", "0"],
    ["10-3", "10333", "황*은", "0"],
    ["10-3", "10334", "황*인", "0"],
    ["10-4", "10401", "강*재", "0"],
    ["10-4", "10402", "고*아", "0"],
    ["10-4", "10403", "권*연", "0"],
    ["10-4", "10404", "김*은", "0"],
    ["10-4", "10405", "김*연", "0"],
    ["10-4", "10406", "김*현", "0"],
    ["10-4", "10407", "김*원", "0"],
    ["10-4", "10408", "김*은", "0"],
    ["10-4", "10409", "김*혁", "0"],
    ["10-4", "10410", "김*휘", "0"],
    ["10-4", "10411", "김*이미", "0"],
    ["10-4", "10412", "노*윤", "0"],
    ["10-4", "10413", "리*비", "0"],
    ["10-4", "10414", "배*균", "0"],
    ["10-4", "10415", "배*민", "0"],
    ["10-4", "10416", "백*훈", "0"],
    ["10-4", "10417", "서*기", "0"],
    ["10-4", "10418", "신*원", "0"],
    ["10-4", "10419", "윤*일", "0"],
    ["10-4", "10420", "윤*준", "0"],
    ["10-4", "10421", "윤*진", "0"],
    ["10-4", "10422", "이*나", "0"],
    ["10-4", "10423", "이*희", "0"],
    ["10-4", "10424", "이*수", "0"],
    ["10-4", "10425", "임*현", "0"],
    ["10-4", "10426", "임*한", "0"],
    ["10-4", "10427", "임*하", "0"],
    ["10-4", "10428", "장*아", "0"],
    ["10-4", "10429", "장*성", "0"],
    ["10-4", "10430", "전*훈", "0"],
    ["10-4", "10431", "정*완", "0"],
    ["10-4", "10432", "조*희", "0"],
    ["10-4", "10433", "최*아", "0"],
    ["10-4", "10434", "최*윤", "0"],
    ["10-5", "10501", "강*연", "0"],
    ["10-5", "10502", "구*미", "0"],
    ["10-5", "10503", "김*희", "0"],
    ["10-5", "10504", "김*선", "0"],
    ["10-5", "10505", "김*경", "0"],
    ["10-5", "10506", "김*린", "0"],
    ["10-5", "10507", "김*율", "0"],
    ["10-5", "10508", "김*건", "0"],
    ["10-5", "10509", "박*찬", "0"],
    ["10-5", "10510", "박*준", "0"],
    ["10-5", "10511", "박*슬", "0"],
    ["10-5", "10512", "양*희", "0"],
    ["10-5", "10513", "오*", "0"],
    ["10-5", "10514", "유*우", "0"],
    ["10-5", "10515", "유*나", "0"],
    ["10-5", "10516", "이*현", "0"],
    ["10-5", "10517", "이*아", "0"],
    ["10-5", "10518", "임*찬", "0"],
    ["10-5", "10519", "임*윤", "0"],
    ["10-5", "10520", "임*혁", "0"],
    ["10-5", "10521", "임*진", "0"],
    ["10-5", "10522", "장*원", "0"],
    ["10-5", "10523", "전*온", "0"],
    ["10-5", "10524", "정*현", "0"],
    ["10-5", "10525", "정*용", "0"],
    ["10-5", "10526", "정*훈", "0"],
    ["10-5", "10527", "정*연", "0"],
    ["10-5", "10528", "조*서", "0"],
    ["10-5", "10529", "차*늘", "0"],
    ["10-5", "10530", "최*랑", "0"],
    ["10-5", "10531", "최*아", "0"],
    ["10-5", "10532", "최*호", "0"],
    ["10-5", "10533", "홍*원", "0"],
    ["10-5", "10534", "황*훈", "0"],
    ["11-1", "11101", "강*재", "0"],
    ["11-1", "11102", "구*현", "0"],
    ["11-1", "11103", "기*윤", "0"],
    ["11-1", "11104", "김*훈", "0"],
    ["11-1", "11105", "김*민", "0"],
    ["11-1", "11106", "김*남", "0"],
    ["11-1", "11107", "김*현", "0"],
    ["11-1", "11108", "김*빈", "0"],
    ["11-1", "11109", "김*수", "0"],
    ["11-1", "11110", "김*서", "0"],
    ["11-1", "11111", "김*진", "0"],
    ["11-1", "11112", "노*영", "0"],
    ["11-1", "11113", "박*림", "0"],
    ["11-1", "11114", "박*미", "0"],
    ["11-1", "11115", "배*희", "0"],
    ["11-1", "11116", "백*열", "0"],
    ["11-1", "11117", "서*원", "0"],
    ["11-1", "11118", "설*진", "0"],
    ["11-1", "11119", "손*영", "0"],
    ["11-1", "11120", "송*우", "0"],
    ["11-1", "11121", "심*민", "0"],
    ["11-1", "11122", "우*정", "0"],
    ["11-1", "11123", "유*희", "0"],
    ["11-1", "11124", "윤*범", "0"],
    ["11-1", "11125", "이*훈", "0"],
    ["11-1", "11126", "이*희", "0"],
    ["11-1", "11127", "이*기", "0"],
    ["11-1", "11128", "이*현", "0"],
    ["11-1", "11129", "장*희", "0"],
    ["11-1", "11130", "최*서", "0"],
    ["11-1", "11131", "하*지", "0"],
    ["11-1", "11132", "한*진", "0"],
    ["11-2", "11201", "강*현", "0"],
    ["11-2", "11202", "금*준", "0"],
    ["11-2", "11203", "김*영", "0"],
    ["11-2", "11204", "김*준", "0"],
    ["11-2", "11205", "김*령", "0"],
    ["11-2", "11206", "김*연", "0"],
    ["11-2", "11207", "김*곤", "0"],
    ["11-2", "11208", "김*현", "0"],
    ["11-2", "11209", "김*형", "0"],
    ["11-2", "11210", "김*연", "0"],
    ["11-2", "11211", "문*은", "0"],
    ["11-2", "11212", "박*준", "0"],
    ["11-2", "11213", "박*희", "0"],
    ["11-2", "11214", "배*규", "0"],
    ["11-2", "11215", "배*빈", "0"],
    ["11-2", "11216", "서*원", "0"],
    ["11-2", "11217", "송*훈", "0"],
    ["11-2", "11218", "신*주", "0"],
    ["11-2", "11219", "심*우", "0"],
    ["11-2", "11220", "양*조", "0"],
    ["11-2", "11221", "이*규", "0"],
    ["11-2", "11222", "이*나", "0"],
    ["11-2", "11223", "이*현", "0"],
    ["11-2", "11224", "이*나", "0"],
    ["11-2", "11225", "이*영", "0"],
    ["11-2", "11226", "이*령", "0"],
    ["11-2", "11227", "임*진", "0"],
    ["11-2", "11228", "정*준", "0"],
    ["11-2", "11229", "조*영", "0"],
    ["11-2", "11230", "천*민", "0"],
    ["11-2", "11231", "최*솔", "0"],
    ["11-2", "11232", "함*권", "0"],
    ["11-3", "11301", "강*수", "0"],
    ["11-3", "11302", "권*림", "0"],
    ["11-3", "11303", "김*비", "0"],
    ["11-3", "11304", "김*빈", "0"],
    ["11-3", "11305", "김*진", "0"],
    ["11-3", "11306", "김*호", "0"],
    ["11-3", "11307", "김*환", "0"],
    ["11-3", "11308", "김*규", "0"],
    ["11-3", "11309", "김*남", "0"],
    ["11-3", "11310", "김*형", "0"],
    ["11-3", "11311", "박*소", "0"],
    ["11-3", "11312", "박*우", "0"],
    ["11-3", "11313", "박*용", "0"],
    ["11-3", "11314", "방*현", "0"],
    ["11-3", "11315", "배*진", "0"],
    ["11-3", "11316", "백*원", "0"],
    ["11-3", "11317", "배*망", "0"],
    ["11-3", "11318", "성*혁", "0"],
    ["11-3", "11319", "손*우", "0"],
    ["11-3", "11320", "송*오", "0"],
    ["11-3", "11321", "신*수", "0"],
    ["11-3", "11322", "안*현", "0"],
    ["11-3", "11323", "윤*원", "0"],
    ["11-3", "11324", "이*정", "0"],
    ["11-3", "11325", "이*민", "0"],
    ["11-3", "11326", "이*광", "0"],
    ["11-3", "11327", "이*민", "0"],
    ["11-3", "11328", "전*정", "0"],
    ["11-3", "11329", "전*진", "0"],
    ["11-3", "11330", "정*윤", "0"],
    ["11-3", "11331", "정*정", "0"],
    ["11-3", "11332", "제*영", "0"],
    ["11-4", "11401", "구*아", "0"],
    ["11-4", "11402", "김*경", "0"],
    ["11-4", "11403", "김*희", "0"],
    ["11-4", "11404", "김*준", "0"],
    ["11-4", "11405", "김*결", "0"],
    ["11-4", "11406", "김*우", "0"],
    ["11-4", "11407", "김*현", "0"],
    ["11-4", "11408", "김*웅", "0"],
    ["11-4", "11409", "김*울", "0"],
    ["11-4", "11410", "김*정", "0"],
    ["11-4", "11411", "남*연", "0"],
    ["11-4", "11412", "박*형", "0"],
    ["11-4", "11413", "박*연", "0"],
    ["11-4", "11414", "박*얀", "0"],
    ["11-4", "11415", "방*우", "0"],
    ["11-4", "11416", "배*원", "0"],
    ["11-4", "11417", "송*민", "0"],
    ["11-4", "11418", "신*지", "0"],
    ["11-4", "11419", "신*주", "0"],
    ["11-4", "11420", "엄*원", "0"],
    ["11-4", "11421", "윤*준", "0"],
    ["11-4", "11422", "이*진", "0"],
    ["11-4", "11423", "이*엽", "0"],
    ["11-4", "11424", "이*영", "0"],
    ["11-4", "11425", "이*희", "0"],
    ["11-4", "11426", "임*진", "0"],
    ["11-4", "11427", "장*재", "0"],
    ["11-4", "11428", "장*수", "0"],
    ["11-4", "11429", "정*원", "0"],
    ["11-4", "11430", "조*훈", "0"],
    ["11-4", "11431", "주*민", "0"],
    ["11-4", "11432", "최*리", "0"],
    ["11-5", "11501", "권*은", "0"],
    ["11-5", "11502", "길*재", "0"],
    ["11-5", "11503", "김*지", "0"],
    ["11-5", "11504", "김*민", "0"],
    ["11-5", "11505", "김*영", "0"],
    ["11-5", "11506", "김*온", "0"],
    ["11-5", "11507", "문*찬", "0"],
    ["11-5", "11508", "민*기", "0"],
    ["11-5", "11509", "박*령", "0"],
    ["11-5", "11510", "박*원", "0"],
    ["11-5", "11511", "배*영", "0"],
    ["11-5", "11512", "백*은", "0"],
    ["11-5", "11513", "손*태", "0"],
    ["11-5", "11514", "양*민", "0"],
    ["11-5", "11515", "양*영", "0"],
    ["11-5", "11516", "오*우", "0"],
    ["11-5", "11517", "오*주", "0"],
    ["11-5", "11518", "유*호", "0"],
    ["11-5", "11519", "윤*언", "0"],
    ["11-5", "11520", "이*현", "0"],
    ["11-5", "11521", "이*아", "0"],
    ["11-5", "11522", "이*은", "0"],
    ["11-5", "11523", "이*인", "0"],
    ["11-5", "11524", "이*정", "0"],
    ["11-5", "11525", "이*연", "0"],
    ["11-5", "11526", "이*연", "0"],
    ["11-5", "11527", "이*기", "0"],
    ["11-5", "11528", "임*현", "0"],
    ["11-5", "11529", "장*윤", "0"],
    ["11-5", "11530", "천*현", "0"],
    ["11-5", "11531", "최*혁", "0"],
    ["11-5", "11532", "한*아", "0"],
    ["11-5", "11533", "홍*빈", "0"]
]
    return data

# 학생 데이터를 파일에 저장하는 함수
def save_data(file_name, data):
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

# 학생 데이터 파일 이름
file_name = 'stu_data.csv'

# 프로그램 시작 시 데이터 로드
stu_data = load_data(file_name)

def is_integer(number):
    try:
        number = int(number)
        return True
    except ValueError:
        return False





def get_stu_price(category):
    stu_num_list = []
    count = 0
    print("[", category, "]")
    for i in range(len(stu_data)):
        if stu_data[i][0] == category:
            count += 1
            stu_num_list.append(stu_data[i][1])
            print(str(count)+':' ,stu_data[i][1], stu_data[i][2], stu_data[i][3])
    number = input("Number : ")
    while not is_integer(number) or int(number) < 1 or int(number) > count:
        count = 0
        print("Type Error !!")
        print()
        for j in range(len(stu_data)):
            if stu_data[j][0] == category:
                count += 1
                print(str(count)+':' ,stu_data[i][1], stu_data[i][2], stu_data[i][3])
        number = input("Number : ")
    return stu_num_list[int(number) - 1]






def order(grade):
    mileage_list = " "
    print("1 : "+grade+"-1반")
    print("2 : "+grade+"-2반")
    print("3 : "+grade+"-3반")
    print("4 : "+grade+"-4반")
    print("5 : "+grade+"-5반")
    print("9 : 적립 취소")
    mileage = input("Number : ")
    print()
    while mileage != '9':
        while is_integer(mileage) == False or int(mileage) < 1 or int(mileage) > 5:
            print("Type Error !!")
            print()
            print("1 : "+grade+"-1반")
            print("2 : "+grade+"-2반")
            print("3 : "+grade+"-3반")
            print("4 : "+grade+"-4반")
            print("5 : "+grade+"-5반")
            print("9 : 적립 취소")
            mileage = input("Number : ")
            print()
        reicve_price = get_stu_price(grade+"-"+mileage)
        mileage_list = reicve_price
        return mileage_list
    return mileage_list









def cal_order(recive_order):
    sum = 0
    if recive_order != " ":
        for i in range(len(stu_data)):
            if stu_data[i][1] == recive_order:
                print(stu_data[i][1], stu_data[i][2], "님의 현재 마일리지 :", stu_data[i][3])
                point = int(input("적립 마일리지 : "))
                sum = point + int(stu_data[i][3])
                stu_data[i][3] = str(sum)
        return str(sum)
    else:
        return sum







def add_mileage():
    number = " "
    while number != '2':
        print("1 : 마일리지 추가")
        print("2 : 마일리지 종료")
        number = input("Number : ")
        if number == '1':
            print()
            print("1 : 7학년")
            print("2 : 8학년")
            print("3 : 9학년")
            print("4 : 10학년")
            print("5 : 11학년")
            grade = input("Grade Number : ")
            print()
            while is_integer(grade) == False or int(grade) < 1 or int(grade) > 5:
                print('Type Error !!')
                print()
                print("1 : 7학년")
                print("2 : 8학년")
                print("3 : 9학년")
                print("4 : 10학년")
                print("5 : 11학년")
                grade = input("Grade Number : ")
                print()
            cal = int(grade) + 6
            recive_order = order(str(cal))
            recive_cal = cal_order(recive_order)
            if recive_cal != 0:
                print("적립된 마일리지 :", recive_cal)
                print()
        elif number == '2':
            save_data(file_name, stu_data)
        else:
            print("Type Error !!")
            print()






def school_rank():
    int_box = stu_data[0][3]
    str_box = stu_data[0]
    for i in range(1,len(stu_data)):
        if int(int_box) < int(stu_data[i][3]):
            int_box = stu_data[i][3]
            str_box = stu_data[i]
    print("전체 1등 :",str_box)
     
    
        





def get_first_data(category):
    str_box = ""
    int_box = ""
    amount_list = []
    count = 0
    for i in range(0,len(stu_data)):
        if category == stu_data[i][0]:
            amount_list.append(stu_data[i])
            count = count + 1

    int_box = amount_list[0][3]
    str_box = amount_list[0]
    for j in range(1,count):
        if int_box < amount_list[j][3]:
            int_box = amount_list[j][3]
            str_box = amount_list[j]
        
    return str_box


def grade_rank():
    amount_grade_list = [""] * 5
    i = 0
    while i != 5:
        grade_list = [""] * 5

        recive1 = get_first_data(str(i+7)+"-1")
        grade_list[0] = recive1

        recive2 = get_first_data(str(i+7)+"-2")
        grade_list[1] = recive2
 
        recive3 = get_first_data(str(i+7)+"-3")
        grade_list[2] = recive3

        recive4 = get_first_data(str(i+7)+"-4")
        grade_list[3] = recive4

        recive5 = get_first_data(str(i+7)+"-5")
        grade_list[4] = recive5

        max = grade_list[0][3]
        str_box = grade_list[0]
        for j in range(1,len(grade_list)):
            if max < grade_list[j][3]:
                max = grade_list[j][3]
                str_box = grade_list[j]
        amount_grade_list[i] = str_box
        i = i + 1
    return amount_grade_list
    




def class_rank():
    i = 0
    while i != 5:
        print("**"+str(i+7)+"학년**")
        print()
        recive1 = get_first_data(str(i+7)+"-1")
        print(str(i+7)+"-1반 1등 :",recive1)
        print()
        recive2 = get_first_data(str(i+7)+"-2")
        print(str(i+7)+"-2반 1등 :",recive2)
        print()
        recive3 = get_first_data(str(i+7)+"-3")
        print(str(i+7)+"-3반 1등 :",recive3)
        print()
        recive4 = get_first_data(str(i+7)+"-4")
        print(str(i+7)+"-4반 1등 :",recive4)
        print()
        recive5 = get_first_data(str(i+7)+"-5")
        print(str(i+7)+"-5반 1등 :",recive5)
        print()
        i = i + 1


    





    


number = " "
while number != '9':
    print("1 : 마일리지 적립")
    print("2 : 마일리지 랭킹보드")
    print('9 : 프로그램 종료')
    number = input("Number : ")
    print()
    if number == '1':
        add_mileage()
        print()

    elif number == '2':
        print("1 : 전교 1등 확인")
        print("2 : 학년별 1등 확인")
        print("3 : 반별 1등 확인")
        choose = input("Number : ")
        print()
        if choose == '1':
            school_rank()
            print()
        elif choose == '2':
            recive_grade_rank = grade_rank()
            for i in range(0,len(recive_grade_rank)):
                print(str(i+7)+"학년 1등 :",recive_grade_rank[i])
            print()
        elif choose == '3':
            class_rank()
            print()
        else:
            print("Type Error !!")
            print()



    elif number == '9':
        print("Program End !!")

    else:
        print("Type Error !!")
