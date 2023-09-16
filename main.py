import numpy
import random
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, MaxPooling1D, Conv1D, GlobalMaxPooling1D, Dropout,Flatten
from tensorflow.keras import utils
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.callbacks import ModelCheckpoint
import pickle

file_create=open("Создать.txt",'r',encoding='utf-8')
lst_create=[]
lstch=["создать", "изменить", "удалить","использовать","переместить","выйти","вывести"]
lsttrain=[0,1,2,3,4,5,6]
lsttrain = utils.to_categorical(lsttrain, 7)
print(lsttrain)
full_lst=[]
full_lst_answer=[]
lst_create_answer=[]
for line in file_create:
    full_lst.append(line[:len(line)-2])
    full_lst_answer.append(0)
file_create.close()
file_change=open("Изменить.txt",'r',encoding='utf-8')
lst_change=[]
lst_change_answer=[]
for line in file_change:
    full_lst.append(line[:len(line)-2])
    full_lst_answer.append(1)
file_change.close()
file_delete=open("Удалить.txt",'r',encoding='utf-8')
lst_delete=[]
lst_delete_answer=[]
for line in file_delete:
    full_lst.append(line[:len(line) - 2])
    full_lst_answer.append(2)
file_delete.close()
file_use=open("Использовать.txt",'r',encoding='utf-8')
lst_use=[]
lst_use_answer=[]
for line in file_use:
    full_lst.append(line[:len(line) - 2])
    full_lst_answer.append(3)
file_use.close()
file_move=open("Переместить.txt",'r',encoding='utf-8')
lst_move=[]
lst_move_answer=[]
for line in file_move:
    full_lst.append(line[:len(line) - 2])
    full_lst_answer.append(4)
file_move.close()
file_exit=open("Выйти.txt",'r',encoding='utf-8')
lst_exit=[]
lst_exit_answer=[]
for line in file_exit:
    full_lst.append(line[:len(line) - 2])
    full_lst_answer.append(5)
file_exit.close()
file_print=open("Вывести.txt",'r',encoding='utf-8')
lst_print=[]
lst_print_answer=[]
for line in file_print:
    full_lst.append(line[:len(line) - 2])
    full_lst_answer.append(6)
file_print.close()
train_lst_x=numpy.empty(len(full_lst), dtype=object)
train_lst_y=numpy.empty(len(full_lst_answer), dtype=object)
lstcheck=[]
count=0
while len(lstcheck)!=len(full_lst):
    num=random.randint(0,len(full_lst)-1)
    if num not in lstcheck:
        lstcheck.append(num)
        train_lst_x[num]=full_lst[count]
        train_lst_y[num]=full_lst_answer[count]
        count+=1
for elem in train_lst_x:
    print(elem)
train_lst_y=utils.to_categorical(train_lst_y,7)
for elem in train_lst_y:
    print(elem)

num_words=10000
max_len=17
tokenizer = Tokenizer(num_words=num_words)
tokenizer.fit_on_texts(train_lst_x)
print(tokenizer.word_index)
sequences = tokenizer.texts_to_sequences(train_lst_x)
print(sequences[0])
print(train_lst_x[0])
x_train = pad_sequences(sequences, maxlen=max_len)
print(x_train[0])
model = Sequential()
model.add(Embedding(num_words, 64, input_length=max_len))
model.add(Conv1D(250, 5, padding='valid', activation='relu'))
model.add(GlobalMaxPooling1D())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(7, activation='sigmoid'))
model.summary()
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])
history = model.fit(x_train,
                    train_lst_y,
                    epochs=7,
                    batch_size=128,
                    validation_split=0.1)

predictions = model.predict(x_train)
print(predictions[0])
print(numpy.argmax(predictions[0]))

text="выведи эту строку на экран"
sequence = tokenizer.texts_to_sequences([text])
data = pad_sequences(sequence, maxlen=max_len)
result = model.predict(data)
print(result)
print(numpy.argmax(result))
model.save("what_to_do.h5")
with open('tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol=pickle.HIGHEST_PROTOCOL)
