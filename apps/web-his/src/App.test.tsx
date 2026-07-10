import { fireEvent, render, screen } from '@testing-library/react'
import { describe, expect, it } from 'vitest'
import App from './App'

describe('MediSalud HIS navigation', () => {
  it('starts in the operational view and keeps quality as a gerencial module', () => {
    render(<App />)

    expect(screen.getByRole('heading', { name: 'Buenos días, Dra. Cárdenas' })).toBeTruthy()
    expect(screen.queryByText('Arquitectura')).toBeNull()

    fireEvent.click(screen.getByRole('button', { name: 'Calidad y reportes' }))
    expect(screen.getByRole('heading', { name: 'Calidad y reportes' })).toBeTruthy()
  })
})
