import nltk
import textblob
from textblob.classifiers import NaiveBayesClassifier

trainPosNeg= [
    ('I think the government need to increase funding for top universities.', 'pos'),
    ('Because most of the country’s top human resources are from these schools, and increasing funding will allow universities to have better resources for future talent in those countries.', 'pos'),
    ('I don\'t agree with you.', 'neg'),
    ('This behavior is unfair to other normal universities.', 'neg'),
    ("No,The top school students have enter a better platform by fair competition, and deserve better treatment.", 'pos'),
    ('So I think it should be better to invest more money in top universities.', 'pos'),
    ('But the alumni of these good schools have already donated a lot of money to their schools each year, but the average university alumni donate relatively less, so this policy is not reasonable.', 'neg'),
]
trainSubObj= [
    ('I think the government need to increase funding for top universities.', 'sub'),
    ('Because most of the country’s top human resources are from these schools, and increasing funding will allow universities to have better resources for future talent in those countries.', 'obj'),
    ('I don\'t agree with you.', 'sub'),
    ('This behavior is unfair to other normal universities.', 'sub'),
    ("No,The top school students have enter a better platform by fair competition, and deserve better treatment.", 'sub'),
    ('So I think it should be better to invest more money in top universities.','sub'),
    ('But the alumni of these good schools have already donated a lot of money to their schools each year, but the average university alumni donate relatively less, so this policy is not reasonable.', 'obj'),
]
classifyPosNeg = NaiveBayesClassifier(trainPosNeg)
classifySubObj=NaiveBayesClassifier(trainSubObj)
#cl.update(new_train)

textA='''
Jenifer Frank: I think the government need to increase funding for top universities. Because most of the country’s top human resources are from these schools, and increasing funding will allow universities to have better resources for future talent in those countries.
Alan: I don't agree with you. This behavior is unfair to other normal universities.
Jennifer:No,The top school students have enter a better platform by fair competition, and deserve better treatment. So I think it should be better to invest more money in top universities.
Alan: But the alumni of these good schools have already donated a lot of money to their schools each year, but the average university alumni donate relatively less, so this policy is not reasonable.
'''
textB='''
A: I don't think college tuition can be exempted, because a lot of the University's income comes from the student's tuition, and if it is eliminated, it will lead to the interruption of the educational resources in the school.
B: I agree to have their tuition exempted,which allows more students who without enouth money to go to college.
A: Now the country has many policies to help poor students go to university, such as loans. Therefore, the policy of exemption from university tuition fees can not be implemented, and poor students can still enter to university study .
B: But free college tuition can help more students to go to college without pressure.
'''

text=textA

text=text.split("\n")
b=[]
for t in text:
    if(t!=""):
        b.append(textblob.TextBlob(t))


for i in range(len(b)):
    for sen in b[i].sentences:
        print(sen)
        if(sen.sentiment.polarity>0):
            print("赞同")
        else:
            print("反对")
        if(sen.sentiment.subjectivity>=0.5):
            print("论点")
        else:
            print("论据")
        print(sen.sentiment)