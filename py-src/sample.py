#! /usr/bin/env python3

### @file sample.py
### @brief ym_sat のサンプルコード
### @author Yusuke Matsunaga (松永 裕介)
###
### Copyright (C) 2019 Yusuke Matsunaga
### All rights reserved.

from ym_sat import Literal, Bool3, Solver, SolverType, Stats

# SATソルバーの生成
# どのSATソルバを使うかの指定もできるがとりあえず省略
sol = Solver()

# 変数の生成
# 実はここで返される型は変数ではなくリテラル(Literal)である．
# 正のリテラルと変数はほぼ等しいが，リテラルは否定できるが変数は否定できない．
# 論理式では変数ではなくリテラルを用いる．
v1 = sol.new_variable()
v2 = sol.new_variable()
v3 = sol.new_variable()

# 制約式の追加
# タプルもしくはリストを引数にする．
sol.add_clause( (v1, ~v2) )

# このようにリスト変数を指定してもよい．
c2 = []
c2.append(~v1)
c2.append(v3)
sol.add_clause( c2 )

# シングルトンのタプルには最後のカンマが必要．
sol.add_clause( (v2,) )

# 求解
# stat は Bool3 型で Bool3._True, Bool3._False, Bool3._X のいずれか．
# 通常は _True (SAT) か _False(UNSAT) になる．_X は途中で探索を打ち切った場合．
# model は Bool3 のリスト．SATの場合の各々変数の割り当て結果が格納される．
# UNSAT の場合には model は None となる．
stat, model = sol.solve()

print('stat = {}'.format(stat))
print('model = {}'.format(model))
