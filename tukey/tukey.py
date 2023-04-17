from scipy import stats
import statsmodels.stats.multicomp as mc

comp = mc.MultiComparison(df['var'], df['group'])
post_hoc_res = comp.tukeyhsd()
post_hoc_res.summary()

post_hoc_res.plot_simultaneous(ylabel='group', xlabel='Score')