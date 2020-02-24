import daops

CMIP5_ID1 = 'cmip5.output1.MOHC.HadGEM2-ES.rcp85.mon.atmos.Amon.r1i1p1.latest.tas'


def test_subset_t():
    result = daops.subset(CMIP5_ID1,
                          time=('2085-01-01', '2120-12-30'),
                          output_dir='outputs')

def test_subset_t_y_x():
    result = daops.subset(CMIP5_ID1,
                          time=('2085-01-01', '2120-12-30'),
                          space=('-20', '-10', '5', '15'),
                          output_dir='outputs')
