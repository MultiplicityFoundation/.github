---
slug: atomic-language-processing
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: 05-systems/Atomic_Language_Processing.md
  last_synced: '2026-03-20T17:17:15.945612Z'
---

       Atomic Language Processing (ALP) with IFMD:
A Three-Layer Prime–Encoded Formalism with Certified Stability
                           Ryan O. Van Gelder & Tyler Van Osdol

                                        October 13, 2025


                                             Abstract
        We present a practical and mathematically rigorous formulation of Atomic Language
     Processing (ALP) within the IFMD framework. ALP assigns prime-based codes to linguistic
     units and composes them with prime-encoded tensor signatures (PETC) while enforcing
     update stability via Arithmetic Control Engine (ACE) constraints. We formalize a three-layer
     architecture—graphemic (static), grapheme-in-context (lightly dynamic), and lexical/mor-
     phemic (dynamic)—define the algebra, derive stability certificates, and provide reference
     implementations for ranking, isotonic rank adjustment, ACE-constrained assignment, PETC
     composition, and evaluation.


Contents
1 Introduction                                                                                      2

2 Preliminaries                                                                                     2
  2.1 Prime sets and disjointness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .       2
  2.2 PETC composition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        2
  2.3 Association scores and ranks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      2

3 Three-Layer ALP                                                                                   3
  3.1 L1: Graphemic layer (static) . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        3
  3.2 L1.5: Grapheme-in-context (dynamic bridge) . . . . . . . . . . . . . . . . . . . .            3
  3.3 L2/L3: Morphemic and lexical layers . . . . . . . . . . . . . . . . . . . . . . . . .         3

4 Stability via ACE                                                                                 3

5 Algebraic validity (PETC)                                                                         3

6 Algorithms                                                                                        3
  6.1 Isotonic Rank Adjustment . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        3
  6.2 ACE-Constrained Assignment . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          3

7 Reference Implementations                                                                         4
  7.1 Data structures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     4
  7.2 L1 Graphemic encoder . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        4
  7.3 L1.5 Contextual ranking (EMA + isotonic) . . . . . . . . . . . . . . . . . . . . .            5
  7.4 ACE-constrained assignment (churn cap) . . . . . . . . . . . . . . . . . . . . . . .          5
  7.5 Spectral drift (power iteration) . . . . . . . . . . . . . . . . . . . . . . . . . . . .      6

8 Evaluation Protocol                                                                               6



                                                  1
9 Serialization and Registries                                                                   6

10 Theoretical Properties                                                                        7

11 Example Prime Tables (English, illustrative)                                                  7

12 Conclusion                                                                                    7

A Notes on Implementation Details                                                                8

B Minimal Runnable Example (Toy)                                                                 8


1     Introduction
The original ALP idea maps high-frequency linguistic relations to small primes and augments
them with multiplicity-like features. Directly updating primes additively breaks primality and
algebraic meaning. We resolve this by separating (i) an order prime determined by rank, from
(ii) a PETC signature that carries structure via exponents on disjoint feature primes. Learning
occurs by updating association scores and re-ranking, while composition is certified by PETC
invariants. Stability and reproducibility are enforced using ACE-style spectral constraints.

Contributions. (1) A clean algebra for order primes and PETC signatures; (2) a three-layer
ALP architecture; (3) stable re-ranking via EMA + isotonic adjustment + ACE-constrained
assignment; (4) sparse PETC vectors and monoid composition; (5) an evaluation protocol
including churn and algebraic-law metrics.


2     Preliminaries
2.1   Prime sets and disjointness
Let Pord and Ppetc be disjoint sets of primes used for order codes and PETC features, respectively.
All integer materializations use
                                   Y e
                     CZ = pord ·    qi i ,     pord ∈ Pord , qi ∈ Ppetc , ei ∈ Z≥0 .            (1)
                                    i

In-memory, codes remain tuples (pord , σ) with σ ∈ Zd≥0 stored sparsely.

2.2   PETC composition
A PETC signature is an exponent vector σ ∈ Zd≥0 over feature primes {q1 , . . . , qd }. Composition
(tensor product) is vector addition:
                                             σx⊗y = σx + σy .                                   (2)
This yields a commutative monoid (Zd≥0 , +) with identity 0 and supports compile-time validity
checks via linear constraints on exponents.

2.3   Association scores and ranks
For a unit u (e.g., a grapheme-in-context key), define a robust association score R(u) (e.g.,
smoothed PPMI or log-likelihood). Online updates use an exponential moving average (EMA):
                       Rt+1 (u) = βRt (u) + (1 − β) R
                                                    b t+1 (u),        β ∈ [0, 1).               (3)
The order prime pord (u) is determined by the rank of Rt and reassigned after each update.

                                                     2
3     Three-Layer ALP
3.1   L1: Graphemic layer (static)
Units are Unicode grapheme clusters. Order primes are fixed per language by corpus frequency.
PETC features include position (onset/nucleus/coda), stress, morph role (prefix/root/suffix),
and grapheme-to-phoneme (G2P) cluster.

3.2   L1.5: Grapheme-in-context (dynamic bridge)
Keys are tuples u = (g, pos, stress, g2p_cluster) so that domain drift changes ranks meaningfully.
After EMA, we compute an isotonic adjustment Riso   t+1
                                                        that preserves near-monotonicity relative
to the previous order before re-ranking and ACE-constrained assignment.

3.3   L2/L3: Morphemic and lexical layers
Morphemic units (affixes, stems) are lightly dynamic; lexical relations (e.g., lemma–lemma, role
arcs) are fully dynamic. PETC captures morphosyntactic features; order primes are assigned by
ranks of task-specific association scores under ACE constraints.


4     Stability via ACE
Let At be a weighted bipartite matrix (units × contexts) with entries derived from Rt . ACE
imposes a spectral perturbation budget ∥∆A∥2 ≤ ε, which bounds singular value drift by Weyl:

                             |σi (At+1 ) − σi (At )| ≤ ∥At+1 − At ∥2 ≤ ε.                          (4)

We operationalize this by (i) isotonic rank projection, (ii) min-cost assignment with a churn
cap (≤ K swaps), and (iii) rejecting updates that would exceed ε based on a power-iteration
estimate.


5     Algebraic validity (PETC)
Mutually exclusive or constrained features are encoded as linear inequalities on σ. For example,
a tense conflict is captured by epast + efuture ≤ 1. A composition σx + σy is valid iff all constraints
are satisfied.


6     Algorithms
6.1   Isotonic Rank Adjustment
Given scores R and a previous order π t , we compute Riso by projecting onto the set of vectors
that are nearly non-increasing along π t using pool-adjacent-violators with a slack parameter.
This stabilizes ranks prior to assignment.

6.2   ACE-Constrained Assignment
We seek a new permutation π t+1 minimizing total rank displacement subject to a churn budget
K:                          n
                          min                         s.t. |{i : π(i) ̸= i}| ≤ K.                  (5)
                                X
                                      wi |π(i) − i|
                         π∈Sn
                                i=1

A min-cost flow formulation solves (5) efficiently.


                                                       3
     7     Reference Implementations
     7.1   Data structures

                            Listing 1: Sparse PETC vector and code tuple
 1   from dataclasses import dataclass
 2   from typing import Dict , Tuple
 3
 4   FeatureId = int
 5
 6   @dataclass ( frozen = True )
 7   class PETCVec :
 8       exp : Dict [ FeatureId , int ]     # feature_id -> exponent ( >=0)
 9
10         def add ( self , other : " PETCVec " ) -> " PETCVec " :
11             out = dict ( self . exp )
12             for k , v in other . exp . items () :
13                   out [ k ] = out . get (k , 0) + v
14             return PETCVec ( out )
15
16   @dataclass ( frozen = True )
17   class ALPCode :
18       order_prime : int
19       petc : PETCVec
20
21         def compose ( self , other : " ALPCode " ) -> " ALPCode " :
22             return ALPCode (
23                 order_prime = compose_order ( self . order_prime , other .
                       order_prime ) ,
24                 petc = self . petc . add ( other . petc )
25             )
26
27   # Serialization ( UF - encoding ) . PP_order and PP_petc are disjoint prime
        tables .
28   PP_petc : Tuple [ int , ...] = (... ,) # registry - ordered feature primes
29
30   def to_integer ( code : ALPCode ) -> int :
31       n = code . order_prime
32       # Multiply only non - zero exponents ; avoid huge ints unless needed .
33       for idx , q in enumerate ( PP_petc ) :
34           e = code . petc . exp . get ( idx , 0)
35           if e :
36                n *= pow (q , e )
37       return n


     7.2   L1 Graphemic encoder

                                 Listing 2: Graphemic ALP (static)
 1   class GraphemicALP :
 2       def __init__ ( self , order_primes : Dict [ str , int ] , feature_map : Dict [
            str , int ]) :
 3           self . order_primes = order_primes                # e . g . , { ’ e ’:2 , ’ t
                 ’:3 ,...}
 4           self . feature_map = feature_map                  # feature name ->
                 feature_id


                                                 4
 5
 6         def encode ( self , grapheme : str , ctx : dict ) -> ALPCode :
 7             p = self . order_primes [ grapheme ]
 8             exp = {}
 9             exp [ self . feature_map [ ’ position_ ’+ ctx [ ’ position ’ ]]] = 1       #
                   onset / nucleus / coda
10             exp [ self . feature_map [ ’ stress_ ’+ str ( ctx [ ’ stress ’ ]) ]] = 1 #
                   0/1/2
11             exp [ self . feature_map [ ’ morph_ ’+ ctx [ ’ morph_role ’ ]]] = 1        #
                   prefix / root / suffix
12             exp [ self . feature_map [ ’ g2p_ ’+ str ( ctx [ ’ g2p_cluster ’ ]) ]] = 1
13             return ALPCode ( order_prime =p , petc = PETCVec ( exp ) )


     7.3   L1.5 Contextual ranking (EMA + isotonic)

                              Listing 3: EMA + isotonic rank stabilization
 1   import numpy as np
 2
 3   def ema_update ( R_prev : Dict [ tuple , float ] , R_hat : Dict [ tuple , float ] ,
        beta =0.9) :
 4       R = dict ( R_prev )
 5       for k , v in R_hat . items () :
 6            R [ k ] = beta * R . get (k , 0.0) + (1 - beta ) * v
 7       return R
 8
 9   def isotonic_adjust ( R : Dict [ tuple , float ] , order_prev : list [ tuple ] ,
        slack : float =0.0) :
10       # Pool - adjacent - violators on values ordered by order_prev ; optional
              slack
11       vals = np . array ([ R [ k ] for k in order_prev ] , dtype = float )
12       # Simple PAV without slack for brevity
13       n = len ( vals ) ; i = 0
14       while i < n -1:
15           if vals [ i ] < vals [ i +1] - slack :
16                 j = i
17                 while j >= 0 and vals [ j ] < vals [ i +1] - slack :
18                      j -= 1
19                 block = slice ( j +1 , i +2)
20                 m = float ( np . mean ( vals [ block ]) )
21                 vals [ block ] = m
22                 i = max (j , 0)
23           else :
24                 i += 1
25       return { k : v for k , v in zip ( order_prev , vals ) }


     7.4   ACE-constrained assignment (churn cap)

                        Listing 4: Min-cost assignment with churn cap (sketch)
 1   # Given stabilized scores R_iso and previous order , produce a new order
         with <= K swaps .
 2   # Here we sketch : keep top T fixed , allow limited swaps in a candidate
        window .
 3
 4   def c onstra ined_ order ( R_iso : Dict [ tuple , float ] , order_prev : list [ tuple
        ] , K : int = int (0.05*1 e6 ) ) :


                                                   5
 5         # Rank by R_iso
 6         order_new = sorted ( R_iso . keys () , key = lambda k : R_iso [ k ] , reverse =
              True )
 7         # Compute minimal edits under cap K ( greedy windowed )
 8         pos_prev = { k : i for i , k in enumerate ( order_prev ) }
 9         swaps = 0; final = []
10         used = set ()
11         for k in order_new :
12             if k in used : continue
13             if k in pos_prev and abs ( len ( final ) - pos_prev [ k ]) <= 1 and
                   swaps < K :
14                   final . append ( k ) ; used . add ( k )
15             else :
16                   final . append ( k ) ; used . add ( k ) ; swaps += 1
17         return final , swaps


     7.5   Spectral drift (power iteration)

                               Listing 5: Estimate ||A||2 bypoweriteration
 1   import scipy . sparse as sp
 2   import numpy as np
 3

 4   def s p ec t r al _ d ri f t _n o r m ( DeltaA : sp . spmatrix , iters : int = 20) :
 5       n = DeltaA . shape [1]
 6       x = np . random . randn ( n )
 7       x /= np . linalg . norm ( x ) + 1e -12
 8       for _ in range ( iters ) :
 9              y = DeltaA @ x
10              normy = np . linalg . norm ( y )
11              if normy == 0: return 0.0
12              x = ( DeltaA . T @ y )
13              x_norm = np . linalg . norm ( x )
14              if x_norm == 0: break
15              x /= x_norm
16       # Rayleigh quotient estimate
17       return float ( normy )



     8     Evaluation Protocol
     For each layer, report task metrics and stability/compositional metrics:

      • L1: G2P CER, spelling/ocr AUC; PETC-law violations per 1k compositions.

      • L1.5: prime-churn per update (%), spectral-drift@k (top-k singular values).

      • L2: SIGMORPHON inflection F1; contradiction rate (tense/number).

      • L3: SRL / relation-extraction F1 deltas with ALP features.


     9     Serialization and Registries
     Maintain a versioned registry for feature IDs and prime tables. On the wire, emit:




                                                     6
{
    "version": 1,
    "lang": "en",
    "unit": "grapheme|morpheme|lemma",
    "text_span": {"start": 123, "end": 127},
    "order_prime": 37,
    "petc": {"2":1, "11":2, ...} // feature_id -> exponent
}


10     Theoretical Properties
Monoid. With composition defined by (2) and order-prime multiset accumulation, (ALP, ◦) is
a monoid with identity (empty code). Associativity follows from integer addition associativity.

Stability certificate. If ∥∆A∥2 ≤ ε, then by (4) all top-k singular values move by at most ε,
bounding the rank churn needed to maintain order within a budget.


11     Example Prime Tables (English, illustrative)

                           Letter   pord   Letter   pord   Letter   pord
                           e        2      t        3      a        5
                           o        7      i        11     n        13
                           s        17     h        19     r        23
                           d        29     l        31     c        37
                           u        41     m        43     w        47
                           f        53     g        59     y        61
                           p        67     b        71     v        73
                           k        79     j        83     x        89
                           q        97     z        101

             Table 1: Illustrative static order primes for English letters (per L1).



12     Conclusion
This report consolidates ALP into a compositional, prime-encoded framework with certified
stability. The division into static graphemic, dynamic contextual grapheme, and dynamic
morpho-lexical layers preserves mathematical elegance (PETC) and practical learning (ACE).
The accompanying code sketches provide a starting point for production implementations.


Acknowledgments
IFMD framework components: Arithmetic Control Engine (ACE, Tyler Van Osdol) and Prime-
Encoded Tensor Calculus (PETC, Ryan Van Gelder).


References
[1] Tyler Van Osdol. Arithmetic Control Engine (ACE). Technical memorandum.

[2] Ryan Van Gelder. Prime-Encoded Tensor Calculus (PETC). Technical memorandum.

                                                7
     A      Notes on Implementation Details
     Isotonic slack. In practice, use a convex projection or isotonic regression with a temperature
     parameter that trades off fidelity vs. order preservation.

     Assignment solver. A full min-cost flow with churn constraint yields better optimality than
     greedy; the sketch provided is a placeholder for clarity.

     G2P clusters. Initialize with a pronouncing dictionary and allow online clustering (e.g.,
     Dirichlet process) over phoneme posteriors to adapt to domain text.


     B      Minimal Runnable Example (Toy)
     Goal. Demonstrate L1.5 dynamic re-ranking (EMA + constrained assignment) and PETC
     composition on two toy words (cat, city). Pure Python, no external dependencies.

     Code

 1   #   Minimal ALP toy demo ( Python 3.10+)
 2   #   - Dynamically ranks grapheme - in - context keys ( L1 .5)
 3   #   - Encodes PETC vectors ( sparse ) and composes word codes
 4   #   - Prints churn and example codes for ’ cat ’ and ’ city ’
 5

 6
 7   from dataclasses import dataclass
 8   from typing import Dict , Tuple , List
 9   from math import log
10
11

12   # - - - - - - - - - - - - - - - - - - Utilities - - - - - - - - - - - - - - - - - -
13
14
15   def first_n_primes ( n : int ) -> List [ int ]:
16   primes , x = [] , 2
17   def is_prime ( k : int ) -> bool :
18   i = 2
19   while i * i <= k :
20   if k % i == 0: return False
21   i += 1
22   return True
23   while len ( primes ) < n :
24   if is_prime ( x ) : primes . append ( x )
25   x += 1
26   return primes
27
28
29   # PETC vector ( sparse ) : feature_id -> exponent
30   @dataclass ( frozen = True )
31   class PETCVec :
32   exp : Dict [ int , int ]
33   def add ( self , other : " PETCVec " ) -> " PETCVec " :
34   out = dict ( self . exp )
35   for k , v in other . exp . items () :
36   out [ k ] = out . get (k , 0) + v
37   return PETCVec ( out )


                                                                 8
38
39
40   @dataclass ( frozen = True )
41   class ALPCode :
42   order_prime : int
43   petc : PETCVec
44   def compose ( self , other : " ALPCode " ) -> " ALPCode " :



     References
      [1] Tyler Van Osdol. Arithmetic control engine (ace). Technical memorandum, 2025.

      [2] Ryan Van Gelder. Prime-encoded tensor calculus (petc). Technical memorandum, 2025.

      [3] Roger A. Horn and Charles R. Johnson. Matrix Analysis. Cambridge University Press, 2
          edition, 2012.

      [4] G. W. Stewart and Ji-Guang Sun. Matrix Perturbation Theory. Academic Press, 1990.

      [5] Harold W. Kuhn. The hungarian method for the assignment problem. Naval Research
          Logistics Quarterly, 2:83–97, 1955.

      [6] James Munkres. Algorithms for the assignment and transportation problems. Journal of
          the Society for Industrial and Applied Mathematics, 5(1):32–38, 1957.

      [7] Ravindra K. Ahuja, Thomas L. Magnanti, and James B. Orlin. Network Flows: Theory,
          Algorithms, and Applications. Prentice Hall, 1993.

      [8] Richard E. Barlow, David J. Bartholomew, J. M. Bremner, and H. D. Brunk. Statistical
          Inference under Order Restrictions: The Theory and Application of Isotonic Regression.
          Wiley, 1972.

      [9] Miriam Ayer, H. D. Brunk, G. M. Ewing, W. T. Reid, and Edward Silverman. An empirical
          distribution function for sampling with incomplete information. The Annals of Mathematical
          Statistics, 26(4):641–647, 1955.

     [10] Kenneth W. Church and Patrick Hanks. Word association norms, mutual information, and
          lexicography. Computational Linguistics, 16(1):22–29, 1990.

     [11] Ted Dunning. Accurate methods for the statistics of surprise and coincidence. In Proceedings
          of the 31st Annual Meeting of the Association for Computational Linguistics, pages 61–66,
          1993.

     [12] Omer Levy and Yoav Goldberg. Neural word embedding as implicit matrix factorization.
          In Advances in Neural Information Processing Systems (NeurIPS), pages 2177–2185, 2014.

     [13] Omer Levy and Yoav Goldberg. Improving distributional similarity with lessons learned
          from word embeddings. Transactions of the Association for Computational Linguistics,
          3:211–225, 2015.

     [14] Jeffrey Pennington, Richard Socher, and Christopher D. Manning. Glove: Global vectors
          for word representation. In Proceedings of the 2014 Conference on Empirical Methods in
          Natural Language Processing (EMNLP), pages 1532–1543, 2014.

     [15] Ulrike von Luxburg. A tutorial on spectral clustering. Statistics and Computing, 17(4):395–
          416, 2007.

                                                    9
[16] Gene H. Golub and Charles F. Van Loan. Matrix Computations. Johns Hopkins University
     Press, 4 edition, 2013.

[17] Ryan Cotterell, Christo Kirov, John Sylak-Glassman, Gérard Walther, Ekaterina Vylomova,
     Máns Hulden, Keith Hall, Arya D. McCarthy, Garrett Nicolai, et al. The conll–sigmorphon
     2017 shared task: Universal morphological reinflection in 52 languages. In Proceedings of
     the CoNLL SIGMORPHON 2017 Shared Task, 2017.

[18] Joakim Nivre, Marie-Catherine de Marneffe, Filip Ginter, Yoav Goldberg, Jan Hajic,
     Christopher D. Manning, Ryan McDonald, Slav Petrov, Sampo Pyysalo, Natalia Silveira,
     Reut Tsarfaty, and Daniel Zeman. Universal dependencies v1: A multilingual treebank
     collection. In Proceedings of LREC, 2016.

[19] Maximilian Bisani and Hermann Ney. Joint-sequence models for grapheme-to-phoneme
     conversion. Speech Communication, 50(5):434–451, 2008.

[20] Unicode Consortium. Unicode standard annex #29: Unicode text segmentation. https:
     //www.unicode.org/reports/tr29/, 2024. Consult the latest version for details.

[21] Saunders Mac Lane. Categories for the Working Mathematician. Springer, 2 edition, 1998.

[22] G. H. Hardy and E. M. Wright. An Introduction to the Theory of Numbers. Oxford
     University Press, 6 edition, 2008.

[23] Lloyd N. Trefethen and III David Bau. Numerical Linear Algebra. SIAM, 1997.

[24] George Kingsley Zipf. Human Behavior and the Principle of Least Effort. Addison-Wesley,
     1949.

[25] Bob Coecke, Mehrnoosh Sadrzadeh, and Stephen Clark. Mathematical foundations for a
     compositional distributional model of meaning. In Lambek Festschrift. College Publications,
     2010.

[26] Carnegie Mellon University. Cmu pronouncing dictionary (version 0.7b). http://www.
     speech.cs.cmu.edu/cgi-bin/cmudict, 2014.




                                              10
