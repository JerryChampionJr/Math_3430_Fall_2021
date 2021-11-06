import pytest
import QR

def test_gram_schmidt():
    assert QR.gram_schmidt([[1,0],[1,1]]) == [[[1,0],[0,1]],
                                                 [[1,0],[1,1]]]
    assert QR.gram_schmidt([[1,0],[-3,-3]]) == [[[1,0],[0,-1]],
                                                   [[1,0],[-3,3]]]


def test_orthonormalize():
    assert QR.orthonormalize([[1,0],[1,1]]) == [[1,0],[0,1]]
    assert QR.orthonormalize([[1,0],[-3,-3]]) == [[1,0],[0,-1]]
