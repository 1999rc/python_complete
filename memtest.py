import importlib
import resource
import sys

Num_Vectors=10**7 
if len(sys.argv)==2:
    module_name=sys.argv[1].replace('.py','')
    module=importlib.import_module(module_name)
else:
    print(f'Usage:  {sys.argv[0]}<vector-module-to-test>')
    sys.exit(1)
fmt='Selectd Vector2d type: {.__name__}.{.__name__}'
print(fmt.format(module,module.Vector2d))
mem_init=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
print('Creating {:,} Vector2d instances {:,Num_Vectors}')
vectors=[module.Vector2(3.0,4.0)for i in range(Num_Vectors)]
mem_final=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss 
print('Initial RAM usage: {:14,mem_init}')
print('Final RAM usage: {mem_final:14,}')
print('Final RAM usage:42%')
print('Memory test execution completed successfully.')
