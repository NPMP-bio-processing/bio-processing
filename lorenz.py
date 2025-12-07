import tellurium as te


def lorenz(sigma=10, rho=28, beta=8/3, x0=1, y0=1, z0=1, t_end=50, points=5000):
    model = te.loada(f'''
        model lorenz
            x' = {sigma} * (y - x)
            y' = x * ({rho} - z) - y
            z' = x * y - {beta} * z
            
            x = {x0}; y = {y0}; z = {z0}
        end
    ''')
    result = model.simulate(0, t_end, points)
    model.plot(result)
    return result

lorenz()