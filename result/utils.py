from .models import QSUBJECT, BTUTOR, TUTOR_HOME#, SESSION#, OVERALL_ANNUAL, ANNUAL
from django.shortcuts import render#, redirect#, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import redirect
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
import xhtml2pdf.pisa as pisa
import time
from datetime import timedelta
from django.contrib import messages
from django.db.models import Avg

def session():
    return '2024'

def tutor_model_summary(request, pk):
    start_time = time.time()
    mains = QSUBJECT.objects.filter(tutor__session__exact=session)
    tutors = [i[0] for i in list(set(list(mains.values_list('tutor')))) if i[0] != None]
    for i in range(0, len(tutors)):#
        t = BTUTOR.objects.get(pk=tutors[i])
        avg = round(QSUBJECT.objects.filter(tutor__subject__exact=t.subject, tutor__Class__exact=t.Class, tutor__term__exact=t.term).aggregate(Avg('agr'))['agr__avg'],2)
        count = QSUBJECT.objects.filter(tutor__subject__exact=t.subject, tutor__Class__exact=t.Class, tutor__term__exact=t.term).count()
        t.model_summary = {str(t.teacher_name)+':'+str(t.subject)[:3]+':'+str(t.Class)+':'+str(t.term)+':'+str(count)+':'+str(avg)+'%'}
        t.save()
    elapsed_time_secs = time.time() - start_time
    msg = "Execution took: %s secs (Wall clock time)" % timedelta(seconds=round(elapsed_time_secs))
    messages.success(request, msg)
    print(msg)
    return redirect('tutor_model_redirected', pk=pk)
    
    
def tutor_model_redirected(request, pk):
    count_s = QSUBJECT.objects.filter(tutor__session__exact=session).count()
    count_t = BTUTOR.objects.filter(session__exact=session).count()
    page = request.GET.get('page', 1)
    paginator = Paginator(BTUTOR.objects.filter(session__exact=session), 30)
    try:
        all_page = paginator.page(page)
    except PageNotAnInteger:
        all_page = paginator.page(1)
    except EmptyPage:
        all_page = paginator.page(paginator.num_pages)
    return render(request, 'result/student_on_all_subjects_detail.html',  {'all_page': all_page, 'count_t': count_t, 'count_s':count_s, 'pk':pk})



def cader(qry):
    clas = [['', 'JSS 1', 'JSS 2', 'JSS 3', 'SSS 1', 'SSS 2', 'SSS 3'], ['', 'jss_one', 'jss_two', 'jss_three', 'sss_one', 'sss_two', 'sss_three']]
    x = clas[0].index(qry)
    if x <= 3:
        cader = 'j'
    else:
        cader = 's'
    return cader

def listofgrades(cader):#marks in ranges with 5 as class intervals
    e = [26, 31, 's', 'j']
    ds = [[], [], []]
    for i in range(100, 0, -1):#marks 100%
        ds[0].append(i)
    ds[1].append(0)
    for i in range(e[e.index(cader)-2], 100, 5):#12 classes of scores with 75 & 70 as (A1, A) and 39 as F
        ds[1].append(i)
    for i in range(0, len(ds[1])):
        if i <= 11:
          ds[2].append(ds[0][ds[1][i]:ds[1][i+1]])
    return ds[2]

def do_grades(scores, cader):#list
    grd = [[], [], ['A1', 'B2', 'B3', 'C4', 'C5', 'C6', 'D7', 'E8', 'F9', 'F9', 'F9', 'F9'], ['A', 'C', 'C', 'C', 'C', 'P', 'P', 'F', 'F', 'F', 'F', 'F'], [0, 1, 's', 'j']]
    dr = listofgrades(cader)#[0, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96] for junior and [0, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76, 81, 86, 91, 96] for sinior
    done = False;
    while not done:
        s = len(scores)
        if s >= 1:
            for r in range(0, len(dr)):
                if scores[0] in dr[r]:
                    grd[1].append(grd[grd[4].index(cader)][r])
            del(scores[0])
        elif s == 0:
            done = True
    return grd[1]

def sort_pos(testlist):
    global mark_orde
    testlist = sorted(testlist, key=None, reverse=True)
    mark_orde = testlist
    sae = []
    seo = []
    for i in range(0, len(testlist)):
        se = []
        for position, item in enumerate(testlist):
            if item == testlist[i]:
                se.append(position+1)
        seo.append(se)
    for i in range(0, len(seo)):
        sae.append(seo[i][0])
    return sae
#d = [15, 12, 3, 87, 21, 63, 96, 74, 14, 3, 21, 14]
#position indexs
#Locatate each positions
def pos_t(w):
    gov = ['1st', '1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th', '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st', '32nd', '33rd', '34th', '35th', '36th', '37th', '38th', '39th', '40th', '41st', '42nd', '43rd', '44th', '45th', '46th', '47th', '48th', '49th', '50th', '51st', '52nd', '53rd', '54th', '55th', '56th', '57th', '58th', '59th', '60th', '61st', '62nd', '63rd', '64th', '65th', '66th', '67th', '68th', '69th', '70th', '71st', '72nd', '73rd', '74th', '75th', '76th', '77th', '78th', '79th', '80th', '81st', '82nd', '83rd', '84th', '85th', '86th', '87th', '88th', '89th', '90th', '91st', '92nd', '93rd', '94th', '95th', '96th', '97th', '98th', '99th', '100th', '101st', '102nd', '103rd', '104th', '105th', '106th', '107th', '108th', '109th', '110th', '111th', '112th', '113th', '114th', '115th', '116th', '117th', '118th', '119th', '120th', '121st', '122nd', '123rd', '124th', '125th', '126th', '127th', '128th', '129th', '130th', '131st', '132nd', '133rd', '134th', '135th', '136th', '137th', '138th', '139th', '140th', '141st', '142nd', '143rd', '144th', '145th', '146th', '147th', '148th', '149th', '150th', '151st', '152nd', '153rd', '154th', '155th', '156th', '157th', '158th', '159th', '160th', '161st', '162nd', '163rd', '164th', '165th', '166th', '167th', '168th', '169th', '170th', '171st', '172nd', '173rd', '174th', '175th', '176th', '177th', '178th', '179th', '180th', '181st', '182nd', '183rd', '184th', '185th', '186th', '187th', '188th', '189th', '190th', '191st', '192nd', '193rd', '194th', '195th', '196th', '197th', '198th', '199th', '200th', '201st', '202nd', '203rd', '204th', '205th', '206th', '207th', '208th', '209th', '210th', '211th', '212th', '213th', '214th', '215th', '216th', '217th', '218th', '219th', '220th', '221st', '222nd', '223rd', '224th', '225th', '226th', '227th', '228th', '229th', '230th', '231st', '232nd', '233rd', '234th', '235th', '236th', '237th', '238th', '239th', '240th', '241st', '242nd', '243rd', '244th', '245th', '246th', '247th', '248th', '249th', '250th', '251st', '252nd', '253rd', '254th', '255th', '256th', '257th', '258th', '259th', '260th', '261st', '262nd', '263rd', '264th', '265th', '266th', '267th', '268th', '269th', '270th', '271st', '272nd', '273rd', '274th', '275th', '276th', '277th', '278th', '279th', '280th', '281st', '282nd', '283rd', '284th', '285th', '286th', '287th', '288th', '289th', '290th', '291st', '292nd', '293rd', '294th', '295th', '296th', '297th', '298th', '299th', '300th', '301st', '302nd', '303rd', '304th', '305th', '306th', '307th', '308th', '309th', '310th', '311th', '312th', '313th', '314th', '315th', '316th', '317th', '318th', '319th', '320th', '321st', '322nd', '323rd', '324th', '325th', '326th', '327th', '328th', '329th', '330th', '331st', '332nd', '333rd', '334th', '335th', '336th', '337th', '338th', '339th', '340th', '341st', '342nd', '343rd', '344th', '345th', '346th', '347th', '348th', '349th', '350th', '351st', '352nd', '353rd', '354th', '355th', '356th', '357th', '358th', '359th', '360th', '361st', '362nd', '363rd', '364th', '365th', '366th', '367th', '368th', '369th', '370th', '371st', '372nd', '373rd', '374th', '375th', '376th', '377th', '378th', '379th', '380th', '381st', '382nd', '383rd', '384th', '385th', '386th', '387th', '388th', '389th', '390th', '391st', '392nd', '393rd', '394th', '395th', '396th', '397th', '398th', '399th', '400th', '401st', '402nd', '403rd', '404th', '405th', '406th', '407th', '408th', '409th', '410th', '411th', '412th', '413th', '414th', '415th', '416th', '417th', '418th', '419th', '420th', '421st', '422nd', '423rd', '424th', '425th', '426th', '427th', '428th', '429th', '430th', '431st', '432nd', '433rd', '434th', '435th', '436th', '437th', '438th', '439th', '440th', '441st', '442nd', '443rd', '444th', '445th', '446th', '447th', '448th', '449th', '450th', '451st', '452nd', '453rd', '454th', '455th', '456th', '457th', '458th', '459th', '460th', '461st', '462nd', '463rd', '464th', '465th', '466th', '467th', '468th', '469th', '470th', '471st', '472nd', '473rd', '474th', '475th', '476th', '477th', '478th', '479th', '480th', '481st', '482nd', '483rd', '484th', '485th', '486th', '487th', '488th', '489th', '490th', '491st', '492nd', '493rd', '494th', '495th', '496th', '497th', '498th', '499th', '500th', '501st', '502nd', '503rd', '504th', '505th', '506th', '507th', '508th', '509th', '510th', '511th', '512th', '513th', '514th', '515th', '516th', '517th', '518th', '519th', '520th', '521st', '522nd', '523rd', '524th', '525th', '526th', '527th', '528th', '529th', '530th', '531st', '532nd', '533rd', '534th', '535th', '536th', '537th', '538th', '539th', '540th', '541st', '542nd', '543rd', '544th', '545th', '546th', '547th', '548th', '549th', '550th', '551st', '552nd', '553rd', '554th', '555th', '556th', '557th', '558th', '559th', '560th', '561st', '562nd', '563rd', '564th', '565th', '566th', '567th', '568th', '569th', '570th', '571st', '572nd', '573rd', '574th', '575th', '576th', '577th', '578th', '579th', '580th', '581st', '582nd', '583rd', '584th', '585th', '586th', '587th', '588th', '589th', '590th', '591st', '592nd', '593rd', '594th', '595th', '596th', '597th', '598th', '599th', '600th', '601st', '602nd', '603rd', '604th', '605th', '606th', '607th', '608th', '609th', '610th', '611th', '612th', '613th', '614th', '615th', '616th', '617th', '618th', '619th', '620th', '621st', '622nd', '623rd', '624th', '625th', '626th', '627th', '628th', '629th', '630th', '631st', '632nd', '633rd', '634th', '635th', '636th', '637th', '638th', '639th', '640th', '641st', '642nd', '643rd', '644th', '645th', '646th', '647th', '648th', '649th', '650th', '651st', '652nd', '653rd', '654th', '655th', '656th', '657th', '658th', '659th', '660th', '661st', '662nd', '663rd', '664th', '665th', '666th', '667th', '668th', '669th', '670th', '671st', '672nd', '673rd', '674th', '675th', '676th', '677th', '678th', '679th', '680th', '681st', '682nd', '683rd', '684th', '685th', '686th', '687th', '688th', '689th', '690th', '691st', '692nd', '693rd', '694th', '695th', '696th', '697th', '698th', '699th', '700th', '701st', '702nd', '703rd', '704th', '705th', '706th', '707th', '708th', '709th', '710th', '711th', '712th', '713th', '714th', '715th', '716th', '717th', '718th', '719th', '720th', '721st', '722nd', '723rd', '724th', '725th', '726th', '727th', '728th', '729th', '730th', '731st', '732nd', '733rd', '734th', '735th', '736th', '737th', '738th', '739th', '740th', '741st', '742nd', '743rd', '744th', '745th', '746th', '747th', '748th', '749th', '750th', '751st', '752nd', '753rd', '754th', '755th', '756th', '757th', '758th', '759th', '760th', '761st', '762nd', '763rd', '764th', '765th', '766th', '767th', '768th', '769th', '770th', '771st', '772nd', '773rd', '774th', '775th', '776th', '777th', '778th', '779th', '780th', '781st', '782nd', '783rd', '784th', '785th', '786th', '787th', '788th', '789th', '790th', '791st', '792nd', '793rd', '794th', '795th', '796th', '797th', '798th', '799th', '800th', '801st', '802nd', '803rd', '804th', '805th', '806th', '807th', '808th', '809th', '810th', '811th', '812th', '813th', '814th', '815th', '816th', '817th', '818th', '819th', '820th', '821st', '822nd', '823rd', '824th', '825th', '826th', '827th', '828th', '829th', '830th', '831st', '832nd', '833rd', '834th', '835th', '836th', '837th', '838th', '839th', '840th', '841st', '842nd', '843rd', '844th', '845th', '846th', '847th', '848th', '849th', '850th', '851st', '852nd', '853rd', '854th', '855th', '856th', '857th', '858th', '859th', '860th', '861st', '862nd', '863rd', '864th', '865th', '866th', '867th', '868th', '869th', '870th', '871st', '872nd', '873rd', '874th', '875th', '876th', '877th', '878th', '879th', '880th', '881st', '882nd', '883rd', '884th', '885th', '886th', '887th', '888th', '889th', '890th', '891st', '892nd', '893rd', '894th', '895th', '896th', '897th', '898th', '899th', '900th', '901st', '902nd', '903rd', '904th', '905th', '906th', '907th', '908th', '909th', '910th', '911th', '912th', '913th', '914th', '915th', '916th', '917th', '918th', '919th', '920th', '921st', '922nd', '923rd', '924th', '925th', '926th', '927th', '928th', '929th', '930th', '931st', '932nd', '933rd', '934th', '935th', '936th', '937th', '938th', '939th', '940th', '941st', '942nd', '943rd', '944th', '945th', '946th', '947th', '948th', '949th', '950th', '951st', '952nd', '953rd', '954th', '955th', '956th', '957th', '958th', '959th', '960th', '961st', '962nd', '963rd', '964th', '965th', '966th', '967th', '968th', '969th', '970th', '971st', '972nd', '973rd', '974th', '975th', '976th', '977th', '978th', '979th', '980th', '981st', '982nd', '983rd', '984th', '985th', '986th', '987th', '988th', '989th', '990th', '991st', '992nd', '993rd', '994th', '995th', '996th', '997th', '998th', '999th', '1000th']
    dss = []
    for i in range(0, len(w)):
        dss.append(gov[w[i]])
    return dss

def marg_marks_positions(testlist, first_last_th, mark_orde):
    marks = []
    position = []
    marg_list = [marks, position]
    dlist = testlist[:]
    print('element in the lists:')
    print('Marks:', testlist[0], 'Ordered_marks:', mark_orde[0], 'Position:', first_last_th[0])
    done = False;
    while not done:
        n = len(dlist)
        if n >= 1:
            get = dlist[0]
            if get in mark_orde:
                H = mark_orde.index(get)
                position.append(first_last_th[H])
                marks.append(get)
                del(dlist[0])
        elif n == 0:
            done = True
    return marg_list
def do_positions(df):
    testlist = df#mark_list(df)
    w = sort_pos(testlist)
    first_last_th = pos_t(w)
    results = marg_marks_positions(testlist, first_last_th, mark_orde)
    return results[1]
    

class Render:
    @staticmethod
    def render(path: str, params: dict):
        template = get_template(path)
        html = template.render(params)
        response = BytesIO()
        pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response)#"utf-8"
        if not pdf.err:
            return HttpResponse(response.getvalue(), content_type='application/pdf')
        else:
            return HttpResponse("Error Rendering PDF", status=400)



    
def parent_id(tutor):
    tutor_id = [x[0] for x in [list(TUTOR_HOME.objects.filter(tutor__exact=tutor.accounts, teacher_name__exact=tutor.teacher_name).values_list('first_term', 'second_term', 'third_term'))]]
    if tutor.term == '1st Term':
        tutors = TUTOR_HOME.objects.get(first_term = tutor)
        tutors.first_term = None
        tutors.save()
    elif tutor.term == '2nd Term':
        tutors = TUTOR_HOME.objects.get(second_term = tutor)
        tutors.second_term = None
        tutors.save()
    elif tutor.term == '3rd Term':
        tutors = TUTOR_HOME.objects.get(third_term = tutor)
        tutors.third_term = None
        tutors.save()
    return tutor_id[0]



