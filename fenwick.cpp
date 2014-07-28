template<typename T>
struct BITree {
  int maxVal;
  T *tree;
  BITree(int _maxVal) {
    maxVal = _maxVal;
    tree = new T[maxVal + 1];
  }
  int read(int i) {
    T sum = 0;
    while (i > 0){
      sum += tree[i];
      i = i & (i - 1); // remove last digit
    }
    return sum;
  }
  void update(int i, T delta) {
    while (i < maxVal) {
      tree[i] += delta;
      i += i & -i;
    }
  }
};
