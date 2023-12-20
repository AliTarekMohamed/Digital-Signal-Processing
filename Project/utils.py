import numpy as np

def multiply(w, h):
    multiplied_signal = []

    N = len(w)
    
    # Multiplication
    for i in range(N):
        multiplied_signal.append(w[i] * h[i])

    return multiplied_signal

def DFT(signal):
    xOfk = []

    j = 1j
    N = len(signal)

    for k in range(N):
        harmonic_value = 0
        for n in range(N):
            harmonic_value += (signal[n] * np.exp((-j * 2 * np.pi * k * n) / N))
        xOfk.append(harmonic_value)
    return xOfk

def IDFT(signal):
    xOfn = []

    j = 1j
    N = len(signal)

    for n in range(N):
        harmonic_value = 0
        for k in range(N):
            harmonic_value += (1 / N) * (signal[k] * np.exp((j * 2 * np.pi * n * k) / N))
        xOfn.append(np.real(harmonic_value))

    return xOfn

def fast_convolution(x, y):
    xOfk1 = []
    xOfk2 = []
    yOfk = []
    convsignal = []

    N1 = len(x)
    N2 = len(y)
    new_len = N1 + N2 - 1

    for i in range(new_len - len(x)):
        x.append(0)
    for i in range(new_len - len(y)):
        y.append(0)

    # DFT
    xOfk1 = DFT(x)
    xOfk2 = DFT(y)

    # Convolution
    yOfk = multiply(xOfk1, xOfk2)

    # IDFT
    convsignal = IDFT(yOfk)

    return convsignal

def Matching(signal, A_avg, B_avg):
    A_corr = correlation(signal, A_avg)
    B_corr = correlation(signal, B_avg)

    if (A_corr[0] > B_corr[0]):
        print ("A")
    else:
        print ("B")

def correlation(ysignal1, ysignal2):
    r = []
    correlationsignal = []

    N = len(ysignal1)

    for j in range(0, N):
        value = 0
        for n in range(0, N):
            # MUSTN'T APPLY MATCHING ON ZEROS
            # if (ysignal1[n] == 0):
            #     continue
            d = n + j
            if (d >= N):
                d -= N
            value += (ysignal1[n] * ysignal2[d])
        r.append(value / N)

    denominator = 0
    y1square = 0
    y2square = 0

    for i in range(0, N):
        y1square += np.power(ysignal1[i], 2)
        y2square += np.power(ysignal2[i], 2)

    denominator = (np.sqrt(y1square * y2square)) / N

    for i in r:
        correlationsignal.append(i / denominator)

    return correlationsignal

def Auto_Correlation(signal):
    yOfn = []
    yOfk = []

    N = len(signal)

    # DFT
    xOfk = DFT(signal)

    # Auto Correlation
    for i in range(0, N):
        yOfk.append(np.conj(xOfk[i]) * xOfk[i])

    # IDFT
    tmp = IDFT(yOfk)

    yOfn.clear()
    for i in tmp:
        yOfn.append(round(i) / N)

    return yOfn

def DCT(signal):
    dct = []

    N = len(signal)

    for k in range(N):
        dct_values = 0
        for n in range(N):
            dct_values += float(signal[n] * np.cos((np.pi / (4 * N)) * ((2 * n) - 1) * ((2 * k) - 1)))
        dct_values *= float(np.sqrt(2 / N))
        dct.append(dct_values)
    
    return dct

def Window_Method(samplingfreq, transition, attenutation):
    N = 0
    w = []

    if (attenutation <= 21):
        N = np.ceil((samplingfreq * 0.9) / transition)
        if (N % 2 == 0):
            N += 1

        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            w.append(1)

    elif (attenutation <= 44):
        N = np.ceil((samplingfreq * 3.1) / transition)
        if (N % 2 == 0):
            N += 1

        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            w.append(0.5 + (0.5 * np.cos((2 * np.pi * i) / N)))

    elif (attenutation <= 53):
        N = np.ceil((samplingfreq * 3.3) / transition)
        if (N % 2 == 0):
            N += 1

        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            w.append(0.54 + (0.46 * np.cos((2 * np.pi * i) / N)))

    elif (attenutation <= 74):
        N = np.ceil((samplingfreq * 5.5) / transition)
        if (N % 2 == 0):
            N += 1

        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            w.append(0.42 + (0.5 * np.cos((2 * np.pi * i) / (N - 1))) + (0.08 * np.cos((4 * np.pi * i) / (N - 1))))

    return w, int(N)

def filter(signal, filter_type, samplingfreq, transition, attenutation, F1, F2):
    w = []
    h = []
    filter = []
    result = []

    w, N = Window_Method(samplingfreq, transition, attenutation)

    Fc1 = (F1 - (transition / 2)) / samplingfreq
    Fc2 = (F2 + (transition / 2)) / samplingfreq

    if (filter_type == 0): # Low Pass Filter
        Fc1 = (F1 + (transition / 2)) / samplingfreq
        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            if (i == 0):
                h.append(2 * Fc1)
                continue
            h.append(2 * Fc1 * ((np.sin(i * (2 * np.pi * Fc1))) / (i * (2 * np.pi * Fc1))))

    elif (filter_type == 1): # Band Pass Filter
        Fc1 = (F1 - (transition / 2)) / samplingfreq
        Fc2 = (F2 + (transition / 2)) / samplingfreq

        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            if (i == 0):
                h.append(2 * (Fc2 - Fc1))
                continue
            h.append((2 * Fc2 * (np.sin(i * (2 * np.pi * Fc2)) / (i * (2 * np.pi * Fc2)))) - (2 * Fc1 * (np.sin(i * (2 * np.pi * Fc1)) / (i * (2 * np.pi * Fc1)))))

    elif (filter_type == 2): # Band Reject Filter
        Fc1 = (F1 + (transition / 2)) / samplingfreq
        Fc2 = (F2 - (transition / 2)) / samplingfreq

        for i in range(int(0 - ((N-1)/2)), int(((N-1)/2) + 1)):
            if (i == 0):
                h.append(1 - (2 * (Fc2 - Fc1)))
                continue
            h.append((2 * Fc1 * (np.sin(i * (2 * np.pi * Fc1)) / (i * (2 * np.pi * Fc1)))) - (2 * Fc2 * (np.sin(i * (2 * np.pi * Fc2)) / (i * (2 * np.pi * Fc2)))))

    filter = multiply(w, h)
    result = fast_convolution(filter, signal)
    return result

def upsampling(signal, l):
    up_sampled = []
    for i in range(len(signal)):
        up_sampled.append(signal[i])
        if (i == (len(signal) - 1)):
            break
        for j in range(l - 1):
            up_sampled.append(0)

    return up_sampled

def downsampling(signal, m):
    down_sampled = []
    for i in range(len(signal)):
        if ((i % m) == 0):
            down_sampled.append(signal[i])
        else:
            continue

    return down_sampled

def Resampling(signal, M , L, samplingfreq, transition, attenuation, f1, f2):
    filter_type = 0

    if(M == 0 and L != 0):
        temp = upsampling(signal, L)
        result = filter(temp, filter_type, samplingfreq, transition, attenuation, f1, f2)

    elif(M != 0 and L == 0):
        temp = filter(signal, filter_type, samplingfreq, transition, attenuation, f1, f2)
        result = downsampling(temp, M)

    elif(M != 0 and L != 0):
        temp = upsampling(signal, L)
        temp2 = filter(temp, filter_type, samplingfreq, transition, attenuation, f1, f2)
        result = downsampling(temp2, M)

    return result

def Remove_dc(signal):
    dc = []
    for i in signal:
        dc.append(i - np.average(signal))
    return dc

def Normalization(signal):
    a = -1
    b = 1
    normalized = []
    yMin = np.min(signal)
    yMax = np.max(signal)

    for i in range(len(signal)):
        normalized.append(((signal[i] - yMin) * (b - a) / (yMax - yMin)) + a)

    return normalized