Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Users/cambr/.ssh/APPM-4600/Labs/Lab 6/Finite Difference Code.py
Traceback (most recent call last):
  File "C:/Users/cambr/.ssh/APPM-4600/Labs/Lab 6/Finite Difference Code.py", line 27, in <module>
    driver()
  File "C:/Users/cambr/.ssh/APPM-4600/Labs/Lab 6/Finite Difference Code.py", line 10, in driver
    h = 0.01*2**(-np.arange(0,10))
ValueError: Integers to negative integer powers are not allowed.

== RESTART: C:/Users/cambr/.ssh/APPM-4600/Labs/Lab 6/Finite Difference Code.py =
Forward Difference Vector: [-0.99998333 -0.99999583 -0.99999896 -0.99999974 -0.99999993 -0.99999998
 -1.         -1.         -1.         -1.        ]
Centered Difference Vector: [-0.99998333 -0.99999583 -0.99999896 -0.99999974 -0.99999993 -0.99999998
 -1.         -1.         -1.         -1.        ]

== RESTART: C:/Users/cambr/.ssh/APPM-4600/Labs/Lab 6/Finite Difference Code.py =
╒═══════════╤═══════════╤═══════════╤════╤════╤════╤════╤════╤══════════════════════╤═══════════════════════╕
│           │           │           │    │    │    │    │    │   Forward Difference │   Centered Difference │
╞═══════════╪═══════════╪═══════════╪════╪════╪════╪════╪════╪══════════════════════╪═══════════════════════╡
│ -0.999983 │ -0.999996 │ -0.999999 │ -1 │ -1 │ -1 │ -1 │ -1 │                   -1 │                    -1 │
├───────────┼───────────┼───────────┼────┼────┼────┼────┼────┼──────────────────────┼───────────────────────┤
│ -0.999983 │ -0.999996 │ -0.999999 │ -1 │ -1 │ -1 │ -1 │ -1 │                   -1 │                    -1 │
╘═══════════╧═══════════╧═══════════╧════╧════╧════╧════╧════╧══════════════════════╧═══════════════════════╛

== RESTART: C:/Users/cambr/.ssh/APPM-4600/Labs/Lab 6/Finite Difference Code.py =
Traceback (most recent call last):
  File "C:/Users/cambr/.ssh/APPM-4600/Labs/Lab 6/Finite Difference Code.py", line 27, in <module>
    driver()
  File "C:/Users/cambr/.ssh/APPM-4600/Labs/Lab 6/Finite Difference Code.py", line 13, in driver
    print(tabulate(forward_difference(f, s, h), headers = ["Forward Difference"], tablefmt = "fancy_grid") )
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\tabulate\__init__.py", line 2048, in tabulate
    list_of_lists, headers = _normalize_tabular_data(
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\tabulate\__init__.py", line 1471, in _normalize_tabular_data
    rows = list(map(lambda r: r if _is_separating_line(r) else list(r), rows))
  File "C:\Users\cambr\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\site-packages\tabulate\__init__.py", line 1471, in <lambda>
    rows = list(map(lambda r: r if _is_separating_line(r) else list(r), rows))
TypeError: 'numpy.float64' object is not iterable
>>> 
== RESTART: C:/Users/cambr/.ssh/APPM-4600/Labs/Lab 6/Finite Difference Code.py =
Forward Difference Vector: [-0.99998333 -0.99999583 -0.99999896 -0.99999974 -0.99999993 -0.99999998
 -1.         -1.         -1.         -1.        ]
Centered Difference Vector: [-0.99998333 -0.99999583 -0.99999896 -0.99999974 -0.99999993 -0.99999998
 -1.         -1.         -1.         -1.        ]
>>> 
== RESTART: C:/Users/cambr/.ssh/APPM-4600/Labs/Lab 6/Finite Difference Code.py =
Forward Difference Vector: [-0.99998333 -0.99999583 -0.99999896 -0.99999974 -0.99999993 -0.99999998
 -1.         -1.         -1.         -1.        ]
Order of Convergence - Forward: [1, 0.25267199746655056]
Centered Difference Vector: [-0.99998333 -0.99999583 -0.99999896 -0.99999974 -0.99999993 -0.99999998
 -1.         -1.         -1.         -1.        ]
Order of Convergence - Centered: [1, 0.25267286746979567]
>>> 
== RESTART: C:/Users/cambr/.ssh/APPM-4600/Labs/Lab 6/Finite Difference Code.py =
Forward Difference Vector: [-0.99998333 -0.99999583 -0.99999896 -0.99999974 -0.99999993 -0.99999998
 -1.         -1.         -1.         -1.        ]
Order of Convergence - Forward: 1
Centered Difference Vector: [-0.99998333 -0.99999583 -0.99999896 -0.99999974 -0.99999993 -0.99999998
 -1.         -1.         -1.         -1.        ]
Order of Convergence - Centered: 1
