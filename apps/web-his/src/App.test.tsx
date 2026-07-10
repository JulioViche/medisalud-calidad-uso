import { fireEvent, render, screen } from '@testing-library/react'
import { beforeEach, describe, expect, it } from 'vitest'
import App from './App'

function loginAs(email: string) {
  fireEvent.change(screen.getByLabelText('Perfil de demostración'), { target: { value: email } })
  fireEvent.click(screen.getByRole('button', { name: /Ingresar al HIS/ }))
}

describe('MediSalud HIS authentication', () => {
  beforeEach(() => sessionStorage.clear())

  it('starts at login and rejects invalid credentials', () => {
    render(<App />)
    expect(screen.getByRole('heading', { name: 'Iniciar sesión' })).toBeTruthy()

    fireEvent.change(screen.getByLabelText('Contraseña'), { target: { value: 'incorrecta' } })
    fireEvent.click(screen.getByRole('button', { name: /Ingresar al HIS/ }))

    expect(screen.getByRole('alert').textContent).toContain('no son correctos')
  })

  it.each([
    ['medico@medisalud.local', ['Historia clinica', 'Citas y admision', 'Telemedicina'], ['Enfermeria', 'Farmacia', 'Facturacion', 'Reportes operativos']],
    ['enfermeria@medisalud.local', ['Enfermeria', 'Historia clinica'], ['Citas y admision', 'Farmacia', 'Facturacion', 'Reportes operativos']],
    ['admision@medisalud.local', ['Citas y admision', 'Facturacion'], ['Historia clinica', 'Enfermeria', 'Farmacia', 'Reportes operativos']],
    ['farmacia@medisalud.local', ['Farmacia'], ['Historia clinica', 'Enfermeria', 'Citas y admision', 'Facturacion', 'Reportes operativos']],
    ['gerencia@medisalud.local', ['Reportes operativos'], ['Historia clinica', 'Enfermeria', 'Citas y admision', 'Farmacia', 'Facturacion']],
  ])('restricts navigation for %s', (email, visible, hidden) => {
    render(<App />)
    loginAs(email)

    for (const label of visible) expect(screen.getAllByRole('button', { name: label }).length).toBeGreaterThan(0)
    for (const label of hidden) expect(screen.queryAllByRole('button', { name: label })).toHaveLength(0)
  })

  it('persists the session and closes it explicitly', () => {
    const first = render(<App />)
    loginAs('gerencia@medisalud.local')
    expect(screen.getByText('Ing. Daniel Paz')).toBeTruthy()

    first.unmount()
    render(<App />)
    expect(screen.getByText('Ing. Daniel Paz')).toBeTruthy()

    fireEvent.click(screen.getByRole('button', { name: 'Cerrar sesión' }))
    expect(screen.getByRole('heading', { name: 'Iniciar sesión' })).toBeTruthy()
    expect(sessionStorage.getItem('medisalud-his-session')).toBeNull()
  })
})
