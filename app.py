from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('decision_tree_classifier_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel=0
    if request.method == 'POST':
        money_transacted = float(request.form['money_transacted'])
        
        payment_method_other_debit_cards = request.form['payment_method_other_debit_cards']
        if(payment_method_other_debit_cards=='other_debit_cards'):
            payment_method_other_debit_cards = 1
            payment_method_sbi_atm_cum_debit_card = 0
            payment_method_unified_payments_interface = 0
            payment_method_visa_master_credit_cards = 0
            payment_method_visa_master_debit_cards = 0
            
        elif(payment_method_other_debit_cards=='sbi_atm_cum_debit_card'):
            payment_method_sbi_atm_cum_debit_card = 1
            payment_method_other_debit_cards = 0
            payment_method_unified_payments_interface = 0
            payment_method_visa_master_credit_cards = 0
            payment_method_visa_master_debit_cards = 0
            
        elif(payment_method_other_debit_cards=='unified_payments_interface'):
            payment_method_sbi_atm_cum_debit_card = 0
            payment_method_other_debit_cards = 0
            payment_method_unified_payments_interface = 1
            payment_method_visa_master_credit_cards = 0
            payment_method_visa_master_debit_cards = 0
            
        elif(payment_method_other_debit_cards=='visa_master_credit_cards'):
            payment_method_sbi_atm_cum_debit_card = 0
            payment_method_other_debit_cards = 0
            payment_method_unified_payments_interface = 0
            payment_method_visa_master_credit_cards = 1
            payment_method_visa_master_debit_cards = 0
            
        else:
            payment_method_sbi_atm_cum_debit_card = 0
            payment_method_other_debit_cards = 0
            payment_method_unified_payments_interface = 0
            payment_method_visa_master_credit_cards = 0
            payment_method_visa_master_debit_cards = 1
        
            
        partner_category_cat_2 = request.form['partner_category_cat_2']
        if(partner_category_cat_2=='cat_2'):
            partner_category_cat_2 = 1
            partner_category_cat_3 = 0
            partner_category_cat_4 = 0
            partner_category_cat_5 = 0
            partner_category_cat_6 = 0
            partner_category_cat_7 = 0
            partner_category_cat_8 = 0
            partner_category_cat_9 = 0
            
        elif(partner_category_cat_2=='cat_3'):
            partner_category_cat_2 = 0
            partner_category_cat_3 = 1
            partner_category_cat_4 = 0
            partner_category_cat_5 = 0
            partner_category_cat_6 = 0
            partner_category_cat_7 = 0
            partner_category_cat_8 = 0
            partner_category_cat_9 = 0
            
        elif(partner_category_cat_2=='cat_4'):
            partner_category_cat_2 = 0
            partner_category_cat_3 = 0
            partner_category_cat_4 = 1
            partner_category_cat_5 = 0
            partner_category_cat_6 = 0
            partner_category_cat_7 = 0
            partner_category_cat_8 = 0
            partner_category_cat_9 = 0
            
        elif(partner_category_cat_2=='cat_5'):
            partner_category_cat_2 = 0
            partner_category_cat_3 = 0
            partner_category_cat_4 = 0
            partner_category_cat_5 = 1
            partner_category_cat_6 = 0
            partner_category_cat_7 = 0
            partner_category_cat_8 = 0
            partner_category_cat_9 = 0
            
        elif(partner_category_cat_2=='cat_6'):
            partner_category_cat_2 = 0
            partner_category_cat_3 = 0
            partner_category_cat_4 = 0
            partner_category_cat_5 = 0
            partner_category_cat_6 = 1
            partner_category_cat_7 = 0
            partner_category_cat_8 = 0
            partner_category_cat_9 = 0
        
        elif(partner_category_cat_2=='cat_7'):
            partner_category_cat_2 = 0
            partner_category_cat_3 = 0
            partner_category_cat_4 = 0
            partner_category_cat_5 = 0
            partner_category_cat_6 = 0
            partner_category_cat_7 = 1
            partner_category_cat_8 = 0
            partner_category_cat_9 = 0
        
        elif(partner_category_cat_2=='cat_8'):
            partner_category_cat_2 = 0
            partner_category_cat_3 = 0
            partner_category_cat_4 = 0
            partner_category_cat_5 = 0
            partner_category_cat_6 = 0
            partner_category_cat_7 = 0
            partner_category_cat_8 = 1
            partner_category_cat_9 = 0
        
        else:
            partner_category_cat_2 = 0
            partner_category_cat_3 = 0
            partner_category_cat_4 = 0
            partner_category_cat_5 = 0
            partner_category_cat_6 = 0
            partner_category_cat_7 = 0
            partner_category_cat_8 = 0
            partner_category_cat_9 = 1
            
        
        
            
        device_type_ios_devices=request.form['device_type_ios_devices']
        if(device_type_ios_devices=='ios_devices'):
            device_type_ios_devices=1
            device_type_other_pcs=0
            device_type_windows_pcs=0
            
        elif(device_type_ios_devices=='other_pcs'):
            device_type_ios_devices=0
            device_type_other_pcs=1
            device_type_windows_pcs=0
            
        elif(device_type_ios_devices=='windows_pcs'):
            device_type_ios_devices=0
            device_type_other_pcs=0
            device_type_windows_pcs=1
            
        
      
        cred_deb_debit=request.form['cred_deb_debit']
        if(cred_deb_debit=='debit'):
            cred_deb_debit=1
        else:
            cred_deb_debit=0	
            
        partner_pricing_category_1=request.form['partner_pricing_category_1']
        if(partner_pricing_category_1=='1'):
            partner_pricing_category_1=1
            partner_pricing_category_2=0
            partner_pricing_category_4=0
        elif(partner_pricing_category_1=='2'):
            partner_pricing_category_1=0
            partner_pricing_category_2=1
            partner_pricing_category_4=0
        else:
            partner_pricing_category_1=0
            partner_pricing_category_2=0
            partner_pricing_category_4=1
            
         
            
         
            
        prediction=model.predict([[money_transacted,payment_method_other_debit_cards,payment_method_sbi_atm_cum_debit_card,payment_method_unified_payments_interface,payment_method_visa_master_credit_cards,payment_method_visa_master_debit_cards, partner_category_cat_2,partner_category_cat_3, partner_category_cat_4,partner_category_cat_5, partner_category_cat_6,partner_category_cat_7, partner_category_cat_8,partner_category_cat_9, device_type_ios_devices,device_type_other_pcs, device_type_windows_pcs, cred_deb_debit,partner_pricing_category_1, partner_pricing_category_2,partner_pricing_category_4]])
        output=prediction
        if output==1:
            return render_template('index.html',prediction_text="It is a fraudaulant transaction {}".format(output))
        else:
            return render_template('index.html',prediction_text="It is not a fraudaulant transaction")

if __name__=="__main__":
    app.run(debug=True)

