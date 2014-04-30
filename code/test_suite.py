import unittest
import numpy
import computeIGCI
import computeMI
import entropy
from discretizeFluorescenceSignal import discretizeFluorescenceSignal
from computePearsonsCorrelation import computePearsonsCorrelation


# Test
class TestSequenceFunctions( unittest.TestCase ):
    def setUp(self):
         self.seq = 'BOY'
    def test_is_IGCI( self ):
        F = numpy.array([[0, 0], [0, 0]])
        R = numpy.array([[0.0, 0.0], [0.0, 0.0]])
        assert (computeIGCI.computeIGCI(F,'false') == R).all()

    def test_negative_IGCI( self ):
        F = numpy.array([[-10], [-20], [-30], [-40]])
        R = numpy.array([[0]])
        assert (computeIGCI.computeIGCI(F,'false') == R).all()
        
    def test_is_MI( self ):
        F = numpy.array([[0, 0], [0, 0]])
        R = numpy.array([[0.0, 0.0], [0.0, 0.0]])
        assert (computeMI.computeMI(F,'false') == R).all()
        
    def test_is_MI_negative( self ):
        F = numpy.array([[-1, 2], [-2, 4]])
        R = numpy.array([[0.0, 0.0], [0.0, 0.0]])
        assert (computeMI.computeMI(F,'false') == R).all()

    def test_is_MI_different( self ):
        F = numpy.array([[1, 3], [5, 7]])
        R = numpy.array([[0.0, 0.0], [0.0, 0.0]])
        assert (computeMI.computeMI(F,'false') == R).all()
        
    def test_no_entropy( self ):
        F = numpy.array([[2, 2], [2, 2]])
        R = numpy.array([[0], [0]])
        assert (entropy.entropy(F) == R).all()

    def test_negative_entropy( self ):
        F = numpy.array([[-10, -20], [-20, -40]])
        R = numpy.array([[1], [1]])
        assert (entropy.entropy(F) == R).all()

    def test_change_entropy( self ):
        F = numpy.array([[1, 2], [4, 8]])
        R = numpy.array([[1], [1]])
        assert (entropy.entropy(F) == R).all()
        
    def test_is_discretizeFluorescenceSignal( self ):
        F = numpy.array([[-10, 0], [10.0, 20.0]])
        R = numpy.array([[2.0, 2.0]])
        assert (discretizeFluorescenceSignal(F) == R).all()
        
    def test_computePearsonsCorrelation( self ):
        F = numpy.array([[99, 50], [110, 57],\
        [102, 51],[85, 41],[95, 50], [104, 30],\
        [122, 59], [98, 54], [87, 49], [111, 53]])
        R = numpy.array([[0, 0.44376016], [0.44376016, 0]])
        R1 = computePearsonsCorrelation(F,'false')
        assert (numpy.around(R1,decimals = 2) == numpy.around\
                (R,decimals = 2)).all()
        
    def test_computePearsonsCorrelation_negative( self ):
        F = numpy.array([[-99, 50], [-110, 57],\
        [-102, 51],[-85, 41],[-95, 50], [-104, 30],\
        [-122, 59], [-98, 54], [-87, 49], [-111, 53]])
        R = numpy.array([[0, -0.32025631], [-0.32025631, 0]])
        R1 = computePearsonsCorrelation(F,'false')
        assert (numpy.around(R1,decimals = 2) == numpy.around\
                (R,decimals = 2)).all()
    
# Run
if __name__ == '__main__':
    unittest.main()
