# 数据分析DAY04

### 算数平均值

```
S = [s1, s2, s3, s4 .. sn]
m = (s1 + s2 + s3 +..+ sn)/n
```

算数平均值表示对真值的无偏估计.

```python
<1>: np.mean(array)
<2>: ndarray.mean()
```

案例: 计算收盘价的算数平均值

```python
# 计算收盘价的算数平均值
m = np.mean(closing_prices)
mp.hlines(m, dates[0], dates[-1],
          color='orangered', label='AVG',
          linestyle='--')
```

### 加权平均值

算数平均值的每个样本对均值的影响权重是相同的, 但实际业务中每个样本对真值的估计重要性是不同的.

```
S = [s1, s2, s3, s4 .. sn]
W = [w1, w2, w3, w4 .. wn]
m = (s1w1 + s2w2 + s3w3 +..+ snwn)/(w1+w2+..+wn)
```

np提供了API很方便的计算加权平均值:

```python
# array 样本数组
# weight_array  每个样本权重值的数组
np.average(array, weights=weight_array)
```

**(VWAP)成交量加权平均价格**

成交量加权平均值体现了市场对当前交易价格的认可度,VWAP将会更接近这支股票的真实价格.

```python
# 计算成交量加权平均值
vwap = np.average(closing_prices,
                  weights=volumes)
mp.hlines(vwap, dates[0], dates[-1],
          color='limegreen',
          label='VWAP', linestyle='--')
```

**(TWAP)时间加权平均价格**

时间加权平均价格中时间权重越高, 参考意义越大. (越接近当前时间股价的时间权重应该越高)

```python
# 计算时间加权平均值
wprices = dates.astype('M8[D]').astype('int32')
twap = np.average(closing_prices,
                  weights=wprices)
mp.hlines(twap, dates[0], dates[-1],
          color='violet',
          label='TWAP', linestyle='--')
```

### 最值

```python
np.max(array)	# 求数组中的最大值
np.min(array)	# 求数组中的最小值
np.ptp(array)	# 求数组中元素的极差 (max-min)
```

```python
np.argmax(array)	# 求数组最大值的索引位置(下标)
np.argmin(array)	# 求数组最小值的索引位置(下标)
```

```python
# 返回一个新数组. 每个元素从a与b数组中进行选取,选择
# 相应位置较大的值,作为新数组的元素.
np.maximum(a, b)	
# 返回一个新数组. 每个元素从a与b数组中进行选取,选择
# 相应位置较小的值,作为新数组的元素.
np.minimum(a, b)
```

### 中位数

将多个样本按照顺序排列,取中间位置的元素. 

若样本数为奇数,中位数是最中间的元素;若样本数为偶数,中位数是中间两个元素的平均值.

```python
a = [1, 2, 3, 4, 5, 1000]
np.median(a)
# 中位数的算法公式:(a[(size-1)/2] + a[size/2]) / 2
```

案例:

```python
# 获取中位数
median = np.median(sorted_prices)
median2 =   \
    (sorted_prices[int((size - 1) / 2)] +
     sorted_prices[int((size / 2))]) / 2
print(median)
print(median2)
```

### 标准差

```python
S = [s1, s2, s3, ... , sn]	#样本
m = (s1 + s2 + .. + sn) / n #平均值
D = [d1, d2, d3, ... , dn]; di=si-m  #离差
Q = [q1, q2, q3, ... , qn]; qi=di^2  #离差方
V = (q1 + q2 + q3 +...+ qn)/n	#总体方差
S = sqrt(V)	 #总体标准差
```















