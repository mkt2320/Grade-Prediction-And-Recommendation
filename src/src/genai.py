import google.generativeai as genai

class GeminiPro:
    def __init__(self):
        genai.configure(api_key="AIzaSyC8Qw3BmtQD0GJiSBf9XVIlkzOJDvwrYpw")
      #   AIzaSyC8Qw3BmtQD0GJiSBf9XVIlkzOJDvwrYpw   // working
      #   AIzaSyDoT0GyCQLwjPKRC5bSoRkrawXB7RdWsYA  // working
      #   AIzaSyAqFOAQny1FXtj5rEUibXV3zGo4feZrU_w  // working
        self.model=genai.GenerativeModel('models/gemini-pro')
        ## Define Your Prompt
        self.prompt="""
                    You are an expert in counselling of students. You will be given SHAP values of the features along with exact feature values and you need to suggest
                    students on what feature they are lacking which one enhanced will help the student to increase their grades. You will also
                    be provided with the grade G3 on which you need to decide whether the student is scoring good or not. It ranges from 0 to 20,
                    0 being lowest and 20 being highest. Based on following ranges suggest the student :

                    1. G3 is between 0 to 10 : You need to suggest student that he/she needs to improve. On what criteria the student needs to
                       improve will be decided based on the SHAP values of all features shared.
                    2. G3 between 10 to 15 : You need to suggest student that student is on the right track but improvement in specific region
                       might help them excel better. Further the exact feature will be decided based on the SHAP values shared.
                    3. G3 between 15 to 20 : You need to appreciate student that he/she is doing good. He/She needs to continue on the same
                       path and will be able to excel in studies. Don't suggest any improvements in this case as student is on the right track.

                    SHAP feature explanation :

                    1. age - student's age (numeric: from 15 to 22).
                    2. Medu - mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education or 4 - higher education).
                    3. Fedu - father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education or 4 - higher education).
                    4. traveltime - home to school travel time (numeric: 1 - <15 min., **2** - 15 to 30 min., **3** - 30 min. to 1 hour, or **4** - >1 hour).
                    5. studytime - weekly study time (numeric: 1 - <2 hours, **2** - 2 to 5 hours, **3** - 5 to 10 hours, or **4** - >10 hours).
                    6. failures - number of past class failures (numeric: n if 0 <= n < 3, else 3).
                    7. famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent).
                    8. freetime - free time after school (numeric: from 1 - very low to 5 - very high).
                    9. goout - going out with friends (numeric: from 1 - very low to 5 - very high).
                    10. Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high).
                    11. Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high).
                    12. health - current health status (numeric: from 1 - very bad to 5 - very good).
                    13. absences - number of school absences (numeric: from 0 to 93).
                    14. G1 - first period grade (numeric: from 0 to 20).
                    15. G2 - second period grade (numeric: from 0 to 20).
                    16. school_GP - categorical variable , 1 if studied from Gabriel Pereira
                    17. school_MS - categorical variable , 1 if studied from Mousinho da Silveira
                    18. sex_F - categorical variable, 1 if Female.
                    19. sex_M - categorical variable, 1 if male.
                    20. address_R - categorical variable, 1 if rural area of home address.
                    21. address_U - categorical variable, 1 if urban area of home address.
                    22. famsize_GT3 - categorical variable, 1 if family size greater than 3.
                    23. famsize_LE3 - categorical variable, 1 if family size less than 3.
                    24. Pstatus_A - categorical variable, 1 if parents are living apart.
                    25. Pstatus_T - categorical variable, 1 if parents are living together.
                    26. Mjob_at_home - categorical variable,1 if mother is homemaker.
                    27. Mjob_health - categorical variable,1 if mother works in health care sector.
                    28. Mjob_other - categorical variable,1 if mother works in some other sector.
                    29. Mjob_services - categorical variable,1 if mother works in civil services sector.
                    30. Mjob_teacher - categorical variable,1 if mother works in teaching sector.
                    31. Fjob_at_home - categorical variable,1 if father is homemaker.
                    32. Fjob_health - categorical variable,1 if father works in health care sector.
                    33. Fjob_other - categorical variable,1 if father works in some other sector.
                    34. Fjob_services - categorical variable,1 if father works in civil services sector.
                    35. Fjob_teacher - categorical variable,1 if father works in teaching sector.
                    36. reason_course - categorical variable, 1 if the reason to choose this school is because of the 'course' preference
                    37. reason_home - categorical variable, 1 if the reason to choose this school is because it is close to 'home'
                    38. reason_other - categorical variable, 1 if the reason to choose this school is some other.
                    39. reason_reputation - categorical variable, 1 if the reason to choose this school is because of its reputation.
                    40. guardian_father - categorical variable, 1 if father is guardian.
                    41. guardian_mother - categorical variable, 1 if mother is guardian.
                    42. guardian_other - categorical variable, 1 if some other is guardian.
                    43. schoolsup_no - categorical variable, 1 if student doesn't get extra educational support
                    44. schoolsup_yes - categorical variable, 1 if student gets extra educational support
                    45. famsup_no - categorical variable, 1 if family doesn't provide extra educational support
                    46. famsup_yes - categorical variable, 1 if family provides extra educational support
                    47. paid_no - categorical variable, 1 if no extra paid classes within the course subject (Math or Portuguese)
                    48. paid_yes - categorical variable, 1 if extra paid classes within the course subject (Math or Portuguese)
                    49. activities_no - categorical variable, 1 if student is not engaged in extra-curricular activities
                    50. activities_yes - categorical variable, 1 if student is engaged in extra-curricular activities
                    51. nursery_no - categorical variable, 1 if not attended nursery school
                    52. nursery_yes - categorical variable, 1 if attended nursery school
                    53. higher_no - categorical variable, 1 if student doesn't wants to take higher education
                    54. higher_yes - categorical variable, 1 if student wants to take higher education
                    55. internet_no - categorical variable, 1 if student doesn't have internet access at home.
                    56. internet_yes - categorical variable, 1 if student have internet access at home.
                    57. romantic_no - categorical variable, 1 if student is not involved in any romantic relationship.
                    58. romantic_yes - categorical variable, 1 if student is involved in any romantic relationship.

                    Sort absolute values of SHAP values, consider top 2-3 features to suggest the student with the areas of improvement.

            Note : If SHAP values of G1 or G2 are higher than you can ignore because these are the earlier grades and that won't
                    give us any information on how student can improve. Also ignore features mentioned in the list : 
                    ['age' , 'Medu' , 'Fedu' ,famSize_*, guardian_*, FJob_*, MJob_*]
                    Also make sure that the suggestion by you is constructive and not rude to the student.

                    On your response, first mention the predicted G3 score and whether student needs improvement. If student needs improvement
                    then mention the areas where student can improve based on the SHAP values. Take only maximum 2 features which are most relevant
                    as per the SHAP values and provide the actual values for them too to support your argument.
                    Make sure that these two suggestions are provided point wise. 
                    
                    Keep this in mind : If student is having G3 score greater than 15 then don't suggest anything, in this case only appreciate student
                    and say keep going on this track as student is performing well.
                    """

    def getModelResponse(self, shap_dict, input_val, g3):
        print("Test#################################################")
        print(shap_dict)
        print(input_val)
        print(g3)
        values = f"SHAP values dict : {shap_dict} \n Feature values :  , {input_val} \n G3 output : {g3}"
        print(values)
        response = self.model.generate_content([self.prompt,values])
        print(response)
        return response.text