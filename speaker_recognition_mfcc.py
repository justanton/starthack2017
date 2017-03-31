import numpy as np
import layer  # wrapper
import recorded_data
import time
from recorded_data import Source,Target

# LESS IS MORE! :)
# play around with learning_rate and training_iters and batch size
# TODO contribute
learning_rate = 0.001
training_iters = 70  # steps
batch_size = 64


height=20 # mfcc features
width=80 # (max) length of utterance
classes=6 # speakers

batch = word_batch = recorded_data.mfcc_batch_generator(batch_size, source=Source.DIGIT_WAVES, target=Target.speaker)
X, Y = next(batch)
print("batch shape " + str(np.array(X).shape))

shape=[-1, height, width, 1]
# shape=[-1, width,height, 1]


# Densely Connected Convolutional Networks https://arxiv.org/abs/1608.06993  # advanced ResNet
def denseConv(net):
    # type: (layer.net) -> None
    print("Building dense-net")
    net.reshape(shape)  # Reshape input picture
    net.buildDenseConv(nBlocks=1)
    net.classifier() # auto classes from labels


def recurrent(net):
    # type: (layer.net) -> None
    net.rnn()
    net.classifier()


def denseNet(net):
    # type: (layer.net) -> None
    print("Building fully connected pyramid")
    net.reshape(shape)  # Reshape input picture
    net.fullDenseNet()
    net.classifier() # auto classes from labels


# CHOSE MODEL ARCHITECTURE:
# net=layer.net(simple_dense,input_shape=[height,width],output_width=classes, learning_rate=learning_rate) # needs additional parameter alignment
# net=layer.net(model=denseConv,input_width= width*height,output_width=classes, learning_rate=learning_rate) # needs additional parameter alignment
net = layer.net(recurrent, input_shape=[height, width], output_width=classes, learning_rate=learning_rate)

net.train(data=batch,batch_size=10,steps=training_iters,dropout=0.6,display_step=10,test_step=100) # test


speakers = recorded_data.get_speakers()
print('speakers: ' + str(speakers))
demo_mcff = recorded_data.load_mcff_file('Test/sample.wav')  # julia
result = net.predict(demo_mcff, None)
print('detected julia as ' + str(speakers[result]))

demo_mcff = recorded_data.load_mcff_file('Test/sample1.wav') # petra


# while True:
#    time.sleep(20)
# results = net.predict_sort(demo_mcff, None)
# i = 0
# for result in results:
#    i += 1
#    id = results[i]
#    if (len(results) - i) > 0:
#        print('rank in results: ' + str((len(results) - i)) + ' - ' + str(speakers[id]))
#    else:
#        print('detected as speaker from petras voice: ' + str((len(results) - i)) + ' - ' + str(speakers[id]))
