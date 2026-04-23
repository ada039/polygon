jupyter-ada039@juputerub2:~/polyhedron$ find . -name '*.py' -exec pycodestyle {} \;



jupyter-ada039@juputerub2:~/polyhedron$ python -B -m pytest -p no:cacheprovider tests
================================================================================= test session starts =================================================================================
platform linux -- Python 3.12.6, pytest-8.3.4, pluggy-1.5.0
rootdir: /home/jupyter-ada039/polyhedron
plugins: timeout-2.3.1, anyio-4.8.0
collected 39 items                                                                                                                                                                    

tests/test_edge.py ............                                                                                                                                                 [ 30%]
tests/test_facet.py ..........                                                                                                                                                  [ 56%]
tests/test_polygon.py ....                                                                                                                                                      [ 66%]
tests/test_segment.py .............                                                                                                                                             [100%]

================================================================================= 39 passed in 0.10s ==================================================================================



jupyter-ada039@juputerub2:~/polyhedron$ export PYTHONDONTWRITEBYTECODE=yes
jupyter-ada039@juputerub2:~/polyhedron$ coverage run -m pytest -p no:cacheprovider tests && coverage report -m ; rm -f .coverage
================================================================================= test session starts =================================================================================
platform linux -- Python 3.12.6, pytest-8.3.4, pluggy-1.5.0
rootdir: /home/jupyter-ada039/polyhedron
plugins: timeout-2.3.1, anyio-4.8.0
collected 39 items                                                                                                                                                                    

tests/test_edge.py ............                                                                                                                                                 [ 30%]
tests/test_facet.py ..........                                                                                                                                                  [ 56%]
tests/test_polygon.py ....                                                                                                                                                      [ 66%]
tests/test_segment.py .............                                                                                                                                             [100%]

================================================================================= 39 passed in 0.22s ==================================================================================
Name                    Stmts   Miss  Cover   Missing
-----------------------------------------------------
common/r3.py               38     10    74%   60-69
common/tk_drawer.py        32     21    34%   11, 16, 24-30, 34, 38-39, 43-44, 49-55
shadow/polyedr.py         113      8    93%   50, 56, 201-206
tests/test_edge.py         64      2    97%   7, 15
tests/test_facet.py        48      0   100%
tests/test_polygon.py      10      0   100%
tests/test_segment.py      75      0   100%
-----------------------------------------------------
TOTAL                     380     41    89%