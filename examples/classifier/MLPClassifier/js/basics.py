from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.utils import shuffle

from sklearn_porter import Porter

X, y = load_iris(return_X_y=True)

X = shuffle(X, random_state=0)
y = shuffle(y, random_state=0)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=5)

clf = MLPClassifier(
    activation='relu', hidden_layer_sizes=50, max_iter=500, alpha=1e-4,
    solver='sgd', tol=1e-4, random_state=1, learning_rate_init=.1)

clf.fit(X_train, y_train)

# Cheese!

result = Porter(language='js').port(clf)
print(result)

"""
// Array.prototype.fill polyfill:
[].fill||(Array.prototype.fill=function(a){for(var b=Object(this),c=parseInt(b.length,10),d=arguments[1],e=parseInt(d,10)||0,f=0>e?Math.max(c+e,0):Math.min(e,c),g=arguments[2],h=void 0===g?c:parseInt(g)||0,i=0>h?Math.max(c+h,0):Math.min(h,c);i>f;f++)b[f]=a;return b});

var Tmp = function(atts) {

    // Type: relu
    var hidden_activation = function(v) {
        for (var i = 0, l = v.length; i < l; i++) {
            v[i] = Math.max(0, v[i]);
        }
        return v;
    };

    // Type: softmax
    var output_activation = function(v) {
        var max = Number.NEGATIVE_INFINITY;
        for (var i = 0, l = v.length; i < l; i++) {
            if (v[i] > max) {
                max = v[i];
            }
        }
        for (var i = 0, l = v.length; i < l; i++) {
            v[i] = Math.exp(v[i] - max);
        }
        var sum = 0.0;
        for (var i = 0, l = v.length; i < l; i++) {
            sum += v[i];
        }
        for (var i = 0, l = v.length; i < l; i++) {
            v[i] /= sum;
        }
        return v;
    };

    this.predict = function(atts) {
        if (atts.length != 4) { return -1; };

        var activations = [atts, new Array(50).fill(0), new Array(3).fill(0)];
        var coefficients = [[[-0.055317816158370905, -0.25162425407767414, -0.33325197861130057, -0.13177626632767314, -0.23549246545141095, -0.27177010710624283, -0.20915665516342635, 0.015057965302906651, -0.72987930075766605, -0.89266106096451436, -0.053869498543610707, -0.22216066222318268, -0.39899502812673082, -0.28681010148594505, -0.31507011153899617, -0.6703997317135284, -0.46627854428112819, -0.55220519291597547, -0.65753556794341839, -0.2012625909486952, 0.33662471612525191, 0.25425126671040416, -0.12438197591047517, 0.22085158121433773, -0.43004111901974473, 0.12047821481685358, -0.27663295488184064, -0.30729210399464546, -0.2201096819240726, 0.19698947979491854, -0.26776467575302032, -0.55963223046623001, -0.66057684440281694, 0.022109851297338449, 0.05436480230390342, -0.30531205478429857, -0.94689187532840091, -1.1472602273053634, -0.32113622918572421, -0.97806246488102411, 0.12604362195657273, 0.52310425825051154, -0.14636842984592813, -0.11855589566328117, -0.2645119437495197, -0.034737117103522681, -0.057695932963591406, -0.13758846013369239, -0.14148094036584954, -0.24664384043086116], [-0.32041711985049837, -0.043058968510450102, -0.19224497780614169, -0.15629983284213439, -0.0056178077580114668, -0.29775374218304873, 0.04941098010393874, -0.26163930851938133, -0.19756633578664284, -0.58925308366602924, -0.26510631981125071, -0.28998233921283872, -0.0419201891702871, -0.43290432093262493, -0.30002643148337588, -0.48659301663778098, -0.081521874811590178, -0.27842983575218738, -0.039622604256916077, 0.05770247643254544, 0.71332882051710433, -0.36349619254759263, -0.24047875144770522, 0.53045027219372642, -0.59792191320511656, -0.356318569750181, 0.28500135453630931, -0.10148787221769563, 0.16720550745832014, 0.25971388860710037, 0.2555334798063561, -0.10856461864559649, -0.41610950088536136, -0.10073289562774027, -0.35234810455712057, 0.13500748765932857, -0.59236329802269894, -0.6928456596016348, 0.10895932947719877, -0.53435965541922337, -0.28749631798822201, 0.95302314181559844, -0.03339139951489787, -0.21465662301256955, -0.061241193383340838, -0.17531266101796375, 0.032502649222591093, 0.049118905364866981, -0.33141470527927364, 0.078095412793859842], [-0.11556829517891457, -0.28839659290844399, 0.25729079162402252, -0.095152035767087209, 0.27235259530926254, 0.082238817438121087, -0.32278089365740004, 0.61089504167538189, -0.53946895727666411, 0.66336833631954528, -0.21843631503665203, -0.34459111930044772, 0.26988257637824437, 0.22285364019621706, -0.28932878616881214, -0.16019244916792291, -0.15188207190529554, -0.17375211722189438, 0.12003588634597367, -0.25048218839808589, -1.181476027590513, -0.11679924783812019, -0.31445752437419289, -0.71528558652206742, 0.4739675739266182, 0.1429930781072748, 0.035214113037884201, 0.22801710207885825, -0.25054728530241616, -0.55191137079060293, 0.057171971863154362, -0.16787314862568956, -0.35815855192213492, -0.3208968914994626, 0.60992105666976271, -0.22919074588760435, -0.63633627319871755, -0.37091045013710455, 0.24235752387495327, -0.60846958788171768, -0.25014809614706662, -1.0335138637201593, -0.29338371286091719, -0.18073925955574419, -0.3036274299231928, -0.26166657231672047, -0.29878288629035105, 0.14199047853995642, 0.039810711538198082, -0.32495770210408736], [-0.28534610919825071, 0.22769872913725112, 0.045399612503103627, -0.19780148024951577, -0.16511364103110895, 0.16254807942801869, -0.20304390231246003, 0.20984846083539074, 0.05685419958788708, 0.62516653349041584, -0.17343217055411875, -0.022987144452160626, 0.079240581612972052, 0.40417766317485176, -0.22880223204823208, -0.42337014160558756, -0.38940003536068196, -0.17326402738615923, 0.08842740443002832, 0.04590025494515363, -0.54686530359318142, 0.42810346180594094, 0.053162665137136862, -0.32103853894220186, 0.31367095881915363, 0.24999765928913059, 0.11282020075848748, -0.15671789424443483, -0.2891056817821327, -0.28253677782850661, 0.086477013336133002, -0.36053269357622619, 0.086846992712735327, -0.28897125255757344, 0.059892059841316403, 0.19412094475437708, -0.53174460572971327, 0.049633740361929336, 0.016446620815376744, 0.0064188476524307727, -0.26556784617072882, -0.65689592060012647, 0.15670824169328113, 0.25181970948115312, 0.27187307037723824, 0.28797696815559204, -0.36711566037352317, -0.17708922988507345, 0.077851045457767137, 0.29933962842647954]], [[-0.33618760940544834, 0.32081899159033467, -0.083051115109439883], [0.0096383304388566442, 0.2419360820188009, 0.35899310789861344], [0.050274587597035091, 0.086184558536937531, -0.14428921022123034], [0.058431568313521046, 0.16824371439906796, 0.2411152128064154], [0.17164895659196974, 0.13327594625746894, 0.24526414111440331], [-0.11932084344947159, 0.11492655724963714, -0.033057727812256854], [-0.079334977171167304, -0.060016494360769022, -0.066295991899890286], [-0.71486824845646169, 0.16008680648281126, 0.46699990709340716], [-0.083938207334024614, 0.27187161898314255, 0.047703604119507262], [-0.58793523568582373, -0.27887692495314448, 0.91235920748288568], [0.25570703360541275, 0.27175182540995058, 0.10949681033724466], [-0.041009631889342278, -0.23307375710751008, 0.19163291322703432], [-0.15189717246377263, -0.025154028942508202, 0.44780865283409299], [-0.3115278729955171, -0.0056627446166143246, 0.66915144386447312], [0.046335662746525126, -0.023074380835666274, -0.10585719439044175], [-0.070740857338026999, -0.51355079283235072, -0.071290569035165757], [0.31604404174783435, -0.21123109460406667, 0.21568944659130201], [-0.19292113469545474, 0.13803331731090354, 0.48075587735422864], [-0.039151124981216832, -0.35635262270414053, 0.040892690463512495], [-0.18502508791073968, 0.06225274230793363, -0.12632668189370647], [1.3423577687187589, -0.73226914108310381, -0.21773848562508963], [-0.25166254943541461, -0.10212412903127061, -0.11494109237158751], [0.1538190166683838, -0.19636071211303363, -0.16955231982502666], [0.69624421451106, -0.21575476077610575, -0.22195121116483685], [-0.67316493619822226, -0.25154862675007322, 0.48832090783943893], [-0.60011861521328647, 0.22897217494907759, 0.20400673019934881], [0.029615125302479721, 0.10372152966977911, -0.23919109178136511], [0.16925716226788123, -0.18703765803400574, 0.013022157605494675], [0.1919803411529804, -0.32143163003060055, -0.11818935970200066], [0.80761667938359993, -0.33839244383018519, 0.039549307829734537], [0.24669667496849926, 0.30268177307271782, 0.21964458163057088], [-0.14219315348518169, -0.1147780335070106, 0.32706428493072143], [0.30427505815686318, -0.2424714253019345, 0.35094508479670405], [-0.31319460193132892, 0.18184804315717218, 0.15593394728341345], [-0.68983159483189771, 0.15504602360039299, 0.29863974148792627], [-0.082896141260148104, 0.18651145103423833, -0.044376894020555085], [-0.065412112288315574, 0.1944647325415538, 0.25684436618993894], [0.74747044101940641, -1.0212095046332008, 0.33152483608646377], [0.3194605228960728, 0.091923324270713175, 0.3323621136813108], [-0.2826594051060749, -0.29937990221663691, 0.38549704422299341], [-0.36478754627854076, -0.14371799448150668, -0.13593364762469248], [0.9447018816870989, -0.48391730610634243, -0.70129832484415211], [0.24382869144366329, 0.12965597232536735, 0.12848807536103687], [0.25456653136274154, -0.29157794873701726, -0.15670873719185627], [0.32956189577408246, -0.19924632055817562, -0.16975463655496348], [-0.16003760303725742, 0.16834508896389047, -0.02895200248099724], [0.79191574248070362, -0.94258942667724976, -0.33557168526432885], [0.20093565667960181, -0.13637901222029258, -0.31788160371143598], [0.062872216044461984, 0.2313758213174964, -0.080066186818751758], [0.16813372423064626, 0.0074972820959486042, 0.027557136131471489]]];
        var intercepts = [[0.30011741283138643, -0.029751221601027639, 0.27707089984418304, 0.09437747263089169, -0.073328190572502505, -0.009339555268726818, 0.069540321946648831, 0.030114067358475233, 0.1926469413394869, 0.023144226681433459, -0.070082924717630057, 0.24099343057814002, -0.2575927249328282, -0.39112904027195772, -0.24328056130217912, -0.13877438337256462, -0.3840609961969641, 0.20571932163518283, 0.12990256746838588, -0.32332067950525173, -0.11080976020947257, -0.14152059389646346, -0.24600210345938872, 0.26790419688164746, -0.29106359813082683, 0.24950761348487629, 0.054676119964720049, 0.25255465627456269, 0.22982296359481452, 0.29374548533376243, -0.026746489455462041, -0.044633956332849806, 0.015346134348148844, -0.1428540988439016, -0.059281796245452337, 0.030997844617798281, -0.48568377250041256, -0.21003762891120722, -0.044215767340361145, 0.018240118057367596, -0.1466920807505617, 0.3996625667878122, 0.051904810189690342, -0.28673053302698287, 0.19195282255033613, 0.074687451363289303, -0.35766933287571323, -0.05320421333257852, 0.11937922437695309, 0.27906785198501721], [0.37658323831187651, 0.45913319499996325, -0.6367197416049728]];

        for (var i = 0; i < activations.length - 1; i++) {
            for (var j = 0; j < activations[i + 1].length; j++) {
                for (var l = 0; l < activations[i].length; l++) {
                    activations[i + 1][j] += activations[i][l] * coefficients[i][l][j];
                }
                activations[i + 1][j] += intercepts[i][j];
                if ((i + 1) != (activations.length - 1)) {
                    activations[i + 1] = hidden_activation(activations[i + 1]);
                }
            }
        }
        activations[activations.length - 1] = output_activation(activations[activations.length - 1]);

        var class_idx = -1,
            class_val = Number.NEGATIVE_INFINITY;
        for (var i = 0, l = activations[activations.length - 1].length; i < l; i++) {
            if (activations[activations.length - 1][i] > class_val) {
                class_val = activations[activations.length - 1][i];
                class_idx = i;
            }
        }
        return class_idx;
    };

};

if (typeof process !== 'undefined' && typeof process.argv !== 'undefined') {
    if (process.argv.length - 2 == 4) {
        var argv = process.argv.slice(2);
        var prediction = new Tmp().predict(argv);
        console.log(prediction);
    }
}
"""
