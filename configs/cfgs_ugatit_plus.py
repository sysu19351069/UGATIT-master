from easydict import EasyDict

cfgs = {
    # model
    'inc': 3,
    'outc': 3,
    'ngf': 64,
    'ndf': 64,
    'z_dim': 32,
    'use_dropout': False,
    'n_blocks': 4,
    'd_layers': 6,
    'training': True,
    # dataset
    'anime': True,
    'dirA': 'datasets/trainA',
    'dirB': 'datasets/trainB',
    'direction': 'AtoB',
    'load_size': 256,
    'batchsize': 1,
    'worker': 5,
    'resume': '',   # resume training.
    'start_epoch': 0,  # if resume, please set start epoch.
    # training
    'total_epoch': 100,
    'tensorboard': 'log/ugatit_plus',
    'saved_dir': 'log/ckpt_ugatit_plus',
    'pool_size': 10,
    'gan_mode': 'lsgan',
    'lr': 2e-4,
    'beta1': 0.5,
    'lr_decay_epoch': 50,
    'lr_policy': 'linear',
    'lambda_identity': 10,
    'lambda_cycle': 10,
    'lambda_cam': 1000,
    'lambda_similarity': 1.0,  # 或许可以更小
}
cfgs = EasyDict(cfgs)


test_cfgs = EasyDict({
    # model
    'inc': 3,
    'outc': 3,
    'ngf': 64,
    'ndf': 64,
    'z_dim': 32,
    'use_dropout': False,
    'n_blocks': 4,
    'd_layers': 6,
    'training': False,
    # 'saved_dir': '/share/yangjie08/result_ugatit',


})