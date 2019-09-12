env = Environment()

conan = SConscript('build/SConscript_conan')
env.MergeFlags(conan['conan'])
env.VariantDir('build', 'src', duplicate=0)

prog = env.SConscript('build/SConscript', exports='env')
env.Install('.', prog)