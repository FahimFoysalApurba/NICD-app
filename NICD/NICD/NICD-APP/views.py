from django.shortcuts import render
import pickle
import joblib

# Create your views here.

def index(request):
    return render(request, "index.html")


def getPredictions(dur, proto, service, state, spkts, dpkts, sbytes, dbytes, rate, sttl, dttl, sload, sloss,dloss, sinpkt, swin, stcpb, dtcpb, dwin, dmean, ct_srv_src, ct_state_ttl, ct_dst_ltm, ct_src_dport_ltm, ct_dst_sport_ltm, ct_dst_src_ltm, ct_src_ltm, ct_srv_dst):
    model = pickle.load(open('ml_model_final.sav', 'rb'))
    #scaled = pickle.load(open('scaler.sav', 'rb'))

    prediction = model.predict([
        [dur, proto, service, state, spkts, dpkts, sbytes, dbytes, rate, sttl, dttl, sload, sloss,dloss, sinpkt, swin, stcpb, dtcpb, dwin, dmean, ct_srv_src, ct_state_ttl, ct_dst_ltm, ct_src_dport_ltm, ct_dst_sport_ltm, ct_dst_src_ltm, ct_src_ltm, ct_srv_dst]
    ])
    
    if prediction == 0:
        return 0
    elif prediction == 1:
        return 1
    elif prediction == 2:
        return 2
    elif prediction == 3:
        return 3
    elif prediction == 4:
        return 4
    elif prediction == 5:
        return 5
    elif prediction == 6:
        return 6
    elif prediction == 7:
        return 7
    elif prediction == 8:
        return 8
    elif prediction == 9:
        return 9
    else:
        return 10
    

def result(request):

    #clf= pickle.load('model.pkl')
    #list=[]

    dur=float(request.GET['dur'])
    proto=float(request.GET['proto'])
    service=float(request.GET['service'])
    state=float(request.GET['state'])
    spkts=float(request.GET['spkts'])
    dpkts=float(request.GET['dpkts'])
    sbytes=float(request.GET['sbytes'])
    dbytes=float(request.GET['dbytes'])
    rate=float(request.GET['rate'])
    sttl=float(request.GET['sttl'])
    dttl=float(request.GET['dttl'])
    sload=float(request.GET['sload'])
    sloss=float(request.GET['sloss'])
    dloss=float(request.GET['dloss'])
    sinpkt=float(request.GET['sinpkt'])
    swin=float(request.GET['swin'])
    stcpb=float(request.GET['stcpb'])
    dtcpb=float(request.GET['dtcpb'])
    dwin=float(request.GET['dwin'])
    dmean=float(request.GET['dmean'])
    ct_srv_src=float(request.GET['ct_srv_src'])
    ct_state_ttl=float(request.GET['ct_state_ttl'])
    ct_dst_ltm=float(request.GET['ct_dst_ltm'])
    ct_src_dport_ltm=float(request.GET['ct_src_dport_ltm'])
    ct_dst_sport_ltm=float(request.GET['ct_dst_sport_ltm'])
    ct_dst_src_ltm=float(request.GET['ct_dst_src_ltm'])
    ct_src_ltm=float(request.GET['ct_src_ltm'])
    ct_srv_dst=float(request.GET['ct_srv_dst'])
    #list.append(request.GET['attack_cat'])

 

    ans = getPredictions(dur, proto, service, state, spkts, dpkts, sbytes, dbytes, rate, sttl, dttl, sload, sloss,dloss, sinpkt, swin, stcpb, dtcpb, dwin, dmean, ct_srv_src, ct_state_ttl, ct_dst_ltm, ct_src_dport_ltm, ct_dst_sport_ltm, ct_dst_src_ltm, ct_src_ltm, ct_srv_dst)


    #ans=clf.predict([list])

    return render(request, "result.html", {'ans':ans})
