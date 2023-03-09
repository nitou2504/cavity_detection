from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense


# define CNN
def define_CNN(num_classes, dim):
    filter_size = (3, 3)
    pool_size = (2, 2)
    CNN = Sequential([Conv2D(4, filter_size, 
                        input_shape=(dim, dim, 1)),
                      MaxPooling2D(pool_size),
                      Flatten(),
                      Dense(num_classes, activation='sigmoid'),
                      ])
    
    return CNN

# define DCNN1
def define_DCNN1(num_classes, dim):
    filter_size = (3, 3)
    pool_size = (2, 2)
    DCNN1 = Sequential([
        Conv2D(8, (filter_size), activation='relu', 
                    input_shape=(dim, dim, 1)),
        MaxPooling2D(pool_size=pool_size),
        #
        Conv2D(16, filter_size, activation='relu'),
        MaxPooling2D(pool_size=pool_size),
        #
        Flatten(),
        #
        #Dense(128, activation='relu'),
        #Dense(16, activation='relu'),
        Dense(num_classes, activation='sigmoid')

    ])
    return DCNN1

# define DCNN2
def define_DCNN2(num_classes, dim):
    filter_size = (3, 3)
    pool_size = (2, 2)
    DCNN2 = Sequential([
        Conv2D(8, (filter_size), activation='relu',
                    input_shape=(dim, dim, 1)),
        MaxPooling2D(pool_size=pool_size),
        #
        Conv2D(16, filter_size, activation='relu'),
        MaxPooling2D(pool_size=pool_size),
        #
        Conv2D(32, filter_size, activation='relu'),
        MaxPooling2D(pool_size=pool_size),
        #
        Flatten(),
        #
        #Dense(128, activation='relu'),
        #Dense(32, activation='relu'),
        Dense(num_classes, activation='sigmoid')

    ])
    
    return DCNN2

# define DCNN3
def define_DCNN3(num_classes, dim):
    filter_size = (3, 3)
    pool_size = (2, 2)
    DCNN3 = Sequential([
        Conv2D(8, (filter_size), activation='relu',
                    input_shape=(dim, dim, 1)),
        MaxPooling2D(pool_size=pool_size),
        #
        Conv2D(16, filter_size, activation='relu'),
        MaxPooling2D(pool_size=pool_size),
        #
        Conv2D(32, filter_size, activation='relu'),
        MaxPooling2D(pool_size=pool_size),
        #
        Conv2D(64, filter_size, activation='relu'),
        MaxPooling2D(pool_size=pool_size),
        #
        Flatten(),
        #
        #Dense(128, activation='relu'),
        #Dense(32, activation='relu'),
        Dense(num_classes, activation='sigmoid')

    ])
    
    return DCNN3