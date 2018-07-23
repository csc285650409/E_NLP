import pickle
import textblob
from textblob.classifiers import NaiveBayesClassifier

trainPosNeg = [
    ('I think the government need to increase funding for top universities.', 'pos'),
    ('Because most of the country’s top human resources are from these schools, and increasing funding will allow universities to have better resources for future talent in those countries.', 'pos'),
    ('I don\'t agree with you.', 'neg'),
    ('This behavior is unfair to other normal universities.', 'neg'),
    ("No,The top school students have enter a better platform by fair competition, and deserve better treatment.", 'pos'),
    ('So I think it should be better to invest more money in top universities.', 'pos'),
    ('But the alumni of these good schools have already donated a lot of money to their schools each year, but the average university alumni donate relatively less, so this policy is not reasonable.', 'neg'),
]
trainSubObj = [
    ('I think the government need to increase funding for top universities.', 'sub'),
    ('Because most of the country’s top human resources are from these schools, and increasing funding will allow universities to have better resources for future talent in those countries.', 'obj'),
    ('I don\'t agree with you.', 'sub'),
    ('This behavior is unfair to other normal universities.', 'sub'),
    ("No,The top school students have enter a better platform by fair competition, and deserve better treatment.", 'sub'),
    ('So I think it should be better to invest more money in top universities.', 'sub'),
    ('But the alumni of these good schools have already donated a lot of money to their schools each year, but the average university alumni donate relatively less, so this policy is not reasonable.', 'obj'),
]

# negFile1 = open('负面评价词语（英文）.txt')
# negFile2 = open('负面情感词语（英文）.txt')
# posFile1 = open('正面评价词语（英文）.txt')
# posFile2 = open('正面情感词语（英文）.txt')
# count = 30
# now = 0
# for line in negFile1.readlines():
#     trainPosNeg.append((line, 'neg'))
# for line in negFile2.readlines():
#     trainPosNeg.append((line, 'neg'))
# for line in posFile1.readlines():
#     trainPosNeg.append((line, 'pos'))
# for line in posFile2.readlines():
#     trainPosNeg.append((line, 'pos'))
# negFile1.close()
# negFile2.close()
# posFile1.close()
# posFile2.close()

classifyPosNeg = NaiveBayesClassifier(trainPosNeg)
classifySubObj = NaiveBayesClassifier(trainSubObj)

#用新语料更新分类器
def ClassifyUpdate(classify,newtrain):
    classify.update(newtrain)
    # classify.classify(text)#分类使用方法
    return classify

#保存模型
def SaveModel(classify,filename):
    f=open(filename,'wb')
    pickle.dump(classify,f)
    f.close()

#读取模型
def LoadModel(filename):
    f=open(filename,'rb')
    classify=pickle.load(f)
    f.close()
    return classify

textA = '''
Jenifer Frank: I think the government need to increase funding for top universities. Because most of the country’s top human resources are from these schools, and increasing funding will allow universities to have better resources for future talent in those countries.
Alan: I don't agree with you. This behavior is unfair to other normal universities.
Jennifer:No,The top school students have enter a better platform by fair competition, and deserve better treatment. So I think it should be better to invest more money in top universities.
Alan: But the alumni of these good schools have already donated a lot of money to their schools each year, but the average university alumni donate relatively less, so this policy is not reasonable.
'''
textB = '''
A: I don't think college tuition can be exempted, because a lot of the University's income comes from the student's tuition, and if it is eliminated, it will lead to the interruption of the educational resources in the school.
B: I agree to have their tuition exempted,which allows more students who without enouth money to go to college.
A: Now the country has many policies to help poor students go to university, such as loans. Therefore, the policy of exemption from university tuition fees can not be implemented, and poor students can still enter to university study .
B: But free college tuition can help more students to go to college without pressure.
'''

# text = textA


def ENLP(text):
    text = text.split("\n")
    b = []
    for t in text:
        if t != "":
            # print(t)
            b.append(textblob.TextBlob(t))

    answer = ""
    for i in range(len(b)):
        for sen in b[i].sentences:
            # print(sen)
            answer += str(sen) + "\n<br>"
            if sen.sentiment.polarity > 0:
                # print("赞同")
                answer += "agree\n<br>"
            else:
                # print("反对")
                answer += "disagree\n<br>"
            if sen.sentiment.subjectivity >= 0.5:
                # print("论点")
                answer += "论点\n<br>"
            else:
                # print("论据")
                answer += "论据\n<br>"
            # print(sen.sentiment)
            answer += str(sen.sentiment)+"\n<br>"
    return answer
    # print('train ok')
    #
    # for i in range(len(b)):
    #     for sen in b[i].sentences:
    #         print(sen)
    #         print(classifyPosNeg.classify(sen))
    #         print(classifySubObj.classify(sen))
    #         print(sen.sentiment)

if __name__ == '__main__':
    ENLP(textA)