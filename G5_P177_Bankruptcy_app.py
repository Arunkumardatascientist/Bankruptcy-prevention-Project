 
import pickle
import streamlit as st
 
# loading the trained model
pickle_in_knn = open('G5_P177_Bankruptcy_knn.pkl', 'rb') 
classifier_knn = pickle.load(pickle_in_knn)

pickle_in_lr = open('G5_P177_Bankruptcy_lr.pkl', 'rb') 
classifier_lr = pickle.load(pickle_in_lr)

pickle_in_dt = open('G5_P177_Bankruptcy_dt.pkl', 'rb') 
classifier_dt = pickle.load(pickle_in_dt)

pickle_in_svm = open('G5_P177_Bankruptcy_svm.pkl', 'rb') 
classifier_svm = pickle.load(pickle_in_svm)

pickle_in_rf = open('G5_P177_Bankruptcy_rf.pkl', 'rb') 
classifier_rf = pickle.load(pickle_in_rf)

pickle_in_bag = open('G5_P177_Bankruptcy_bag.pkl', 'rb') 
classifier_bag = pickle.load(pickle_in_bag)

pickle_in_bst = open('G5_P177_Bankruptcy_bst.pkl', 'rb') 
classifier_bst = pickle.load(pickle_in_bst)


@st.cache()
# defining the function which will make the prediction using the data which the user inputs 
def prediction(industrial_risk, management_risk, financial_flexibility, credibility, 
               competitiveness, operating_risk, classifier):   
 
    # Pre-processing user input    
    if industrial_risk == "Low":
        industrial_risk = 0
    elif industrial_risk == "Medium":
        industrial_risk = 0.5
    else:
        industrial_risk = 1
 
    if management_risk == "Low":
        management_risk = 0
    elif management_risk == "Medium":
        management_risk = 0.5
    else:
        management_risk = 1
 
    if financial_flexibility == "Low":
        financial_flexibility = 0
    elif financial_flexibility == "Medium":
        financial_flexibility = 0.5
    else:
        financial_flexibility = 1
        
    if credibility == "Low":
        credibility = 0
    elif credibility == "Medium":
        credibility = 0.5
    else:
        credibility = 1
        
    if competitiveness == "Low":
        competitiveness = 0
    elif competitiveness == "Medium":
        competitiveness = 0.5
    else:
        competitiveness = 1 
        
    if operating_risk == "Low":
        operating_risk = 0
    elif operating_risk == "Medium":
        operating_risk = 0.5
    else:
        operating_risk = 1 
        
        
    # Making predictions 
    if classifier== "K-Nearest Neighbors":
        prediction = classifier_knn.predict( 
            [[industrial_risk, management_risk, 
              financial_flexibility, credibility, competitiveness, operating_risk]])
    elif classifier=="Logistic Regression":
        prediction = classifier_dt.predict( 
            [[industrial_risk, management_risk, 
              financial_flexibility, credibility, competitiveness, operating_risk]])
    elif classifier=="Decision Tree":
        prediction = classifier_dt.predict( 
            [[industrial_risk, management_risk, 
              financial_flexibility, credibility, competitiveness, operating_risk]])
    elif classifier=="Support Vector Machines":
        prediction = classifier_svm.predict( 
            [[industrial_risk, management_risk, 
              financial_flexibility, credibility, competitiveness, operating_risk]])
    elif classifier=="Random Forests":
        prediction = classifier_rf.predict( 
            [[industrial_risk, management_risk, 
              financial_flexibility, credibility, competitiveness, operating_risk]])
    elif classifier=="Bagging":
        prediction = classifier_bag.predict( 
            [[industrial_risk, management_risk, 
              financial_flexibility, credibility, competitiveness, operating_risk]])
    elif classifier=="Boosting(Final)":
        prediction = classifier_bst.predict( 
            [[industrial_risk, management_risk, 
              financial_flexibility, credibility, competitiveness, operating_risk]])
    
    if prediction == 1:
        pred = 'Non-Bankruptcy'
    else:
        pred = 'Bankruptcy'
    return pred
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:black;padding:13px"> 
    <h1 style ="color:red;text-align:center;">G5-P177 Bankruptcy Prevention App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    classifier = st.selectbox('**ML MODEL NAME**',("K-Nearest Neighbors", "Logistic Regression",
                                                  "Decision Tree","Support Vector Machines",
                                                  "Random Forests","Bagging","Boosting(Final)"))
    industrial_risk = st.selectbox('**INDUSTRIAL RISK**',("Low", "Medium", "High"))
    management_risk = st.selectbox('**MANAGEMENT RISK**',("Low", "Medium", "High")) 
    financial_flexibility = st.selectbox('**FINANCIAL FLEXIBILITY**',("Low", "Medium", "High"))
    credibility = st.selectbox('**CREDIBILITY**',("Low", "Medium", "High")) 
    competitiveness = st.selectbox('**COMPETITIVENESS**',("Low", "Medium", "High")) 
    operating_risk = st.selectbox('**OPERATING RISK**',("Low", "Medium", "High")) 
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict"): 
        result = prediction(industrial_risk, management_risk, financial_flexibility, 
                            credibility, competitiveness, operating_risk,classifier) 
        if result == 'Non-Bankruptcy':
            st.success('**The company does not file for Bankruptcy**', icon="✅")
            st.balloons()
        elif result == 'Bankruptcy':
            st.success('**The company files for Bankruptcy**',icon="❌")
        print(result)
     
if __name__=='__main__': 
    main()
