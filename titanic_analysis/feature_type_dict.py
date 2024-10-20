def create_feature_type_dict(df):
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """
    feature_types = {
        'numerical': {
            'continuous': ["Fare"],  # Fill with continuous numerical features
            'discrete': ["PassengerId" "Age", "Sibsp", "Parch", "Fare"]  # Fill with discrete numerical features
        },
        'categorical': {
            'nominal': ["Ticket", "Embarked" ],  # Fill with nominal categorical features
            'ordinal': ["Cabin"]  # Fill with ordinal categorical features
        }
    }

    return feature_types


#PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked

#Passenger ID = numerical discrete
#Survived = categorical = nominal 
#Pclass = Categorical / ordinal
#Name = Categorical / nominal
#Sex = Categorical / nominal
#Age - Numerical / discrete
#SibSp - wtf does this mean? Number of siblings/spouses wtf - Numerical/discrete
#Parch - no of parents/children - numerical / discrete - 
#Ticket no - Categorical Nomnal
#Fare - numerical continuous
#Cabin - categorical/nominal/ciuld be ordinal - dependign on "better if near lifeboats"
#Embarked - categorical/nominal
