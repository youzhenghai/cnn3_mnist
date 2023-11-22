from .cnn3_BN_Npara import CNN3BNNPara
from .cnn3_BN_para import CNN3BNPara
from .cnn3_GN_Npara import CNN3GNNPara
from .cnn3_GN_para import CNN3GNPara
from .cnn3_IN_Npara import CNN3INNPara
from .cnn3_IN_para import CNN3INPara
from .cnn3_LN_Npara import CNN3LNNPara
from .cnn3_LN_para import CNN3LNPara

def build_model(args):
    if args.model_name=='CNN3BNNPara':
        return CNN3BNNPara(args)
    elif args.model_name=='CNN3BNPara':
        return CNN3BNPara(args)
    elif args.model_name=='CNN3GNNPara':
        return CNN3GNNPara(args)
    elif args.model_name=='CNN3GNPara':
        return CNN3GNPara(args)
    elif args.model_name=='CNN3INNPara':
        return CNN3INNPara(args)
    elif args.model_name=='CNN3INPara':
        return CNN3INPara(args)
    elif args.model_name=='CNN3LNNPara':
        return CNN3LNNPara(args)
    elif args.model_name=='CNN3LNPara':
        return CNN3LNPara(args)
    else:
    
        raise NotImplementedError(f'{args.model_name} not implemented!')