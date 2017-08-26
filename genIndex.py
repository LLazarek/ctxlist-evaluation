#!python

benchmarks = [
    {
        'name':'Basic Iteration',
        'code':"""for (Integer el : FEList.list) {
    System.out.println(el);
}""",
        'plot':'simpleIteration.png'
    },
    {
        'name':'CheckStyle Iteration',
        'code':"""for (someObj el : FEList.objList) {
    el.longOperation();
}""",
        'plot':'expensiveIteration.png'
    },
    {
        'name':'Iteration with Feature Condition',
        'code':"""for (Integer el : FEList.list) {
    if (FEList.E1)
        System.out.println(el);
}""",
        'plot':'looptype3.png'
    },
    {
        'name':'Iteration Reading Outer Variable',
        'code':"""Integer n = 42;
for (Integer el : FEList.list) {
    System.out.println(el + n);
}""",
        'plot':'looptype4.png'
    },
    {
        'name':'Iteration Modifying Outer Variable',
        'code':"""Integer sum = 0;
for (Integer el : FEList.list) {
    System.out.println(el);
    sum += el;
}""",
        'plot':'looptype2.png'
    },
    {
        'name':'Finding Element',
        'code':"""FEList.list.indexOf(610);""",
        'plot':'findElement.png'
    },
    {
        'name':'Removing Element',
        'code':"""FEList.list.remove(Integer.valueOf(610));""",
        'plot':'removeElement.png'
    },
    {
        'name':'Random Access',
        'code':"""System.out.println(FEList.list.get(6));""",
        'plot':'randomAccess.png'
    },
    {
        'name':'Remove Index',
        'code':"""System.out.println(FEList.list.remove(6));""",
        'plot':'removeIndex.png'
    },
    {
        'name':'Size Calculation',
        'code':"""FEList.list.size();""",
        'plot':'size.png'
    },
    {
        'name':'Sorting',
        'code':"""FEList.list.sort(new Comparator() {
    @Override
    public int compare(Object o1, Object o2) {
        Integer i1 = (Integer) o1;
        Integer i2 = (Integer) o2;
        return i1 - i2;
    }
});""",
        'plot':'sort.png'
    },
    {
        'name':'Variational Sorting',
        'code':"""Comparator<Integer> c;
if (FEList.E1 || FEList.E50)
    c = new Comparator() {
    @Override
    public int compare(Object o1, Object o2) {
        Integer i1 = (Integer) o1;
        Integer i2 = (Integer) o2;
        return i1 - i2;
    }
};
else
    c = new Comparator() {
    @Override
    public int compare(Object o1, Object o2) {
        Integer i1 = (Integer) o1;
        Integer i2 = (Integer) o2;
        return i2 - i1;
    }
};

FEList.list.sort(c);""",
        'plot':'sortType.png'
    },
    {
        'name':'List Construction',
        'code':"""static void addThisMany(int n, LinkedList<Integer> l, int startValue) {
    for (int i = 0; i < n; i++)
        l.add(100*i + startValue);
}

public static LinkedList<Integer> list;
public static void generate(Integer numFeatures) {
    list = new LinkedList<>();

    int i = 0;
    int startValue = 0;
    if (i++ < numFeatures)
        if (E1) addThisMany(10, list, (startValue++)*10);
    if (i++ < numFeatures)
        if (E2) addThisMany(10, list, (startValue++)*10);
    if (i++ < numFeatures)
        if (E3) addThisMany(10, list, (startValue++)*10);
    // ... So on to E100 ...

    // Ensure that list contains at least ten elements
    addThisMany(10, list, (startValue++)*10);
}""",
        'plot':'memory.png'
    }
]

if __name__ == '__main__':
    md = "# How To Efficiently Process 2^100 List Variations "\
    "- Full Benchmark Results\n"\
    "Full source code of the project is available "\
    "[here](https://github.com/chupanw/vbc/tree/iteration-optimization).\n\n"
    for bench in benchmarks:
        md += "\n## {0}\n### Benchmark code\n```java\n{1}\n```\n\
### Results\n![{0} Plot](./{2})\n\n"\
    .format(bench['name'], bench['code'], bench['plot'])

    with open('index.md', 'w') as f:
        f.write(md)
