import { render, screen } from '@testing-library/react'
import { describe, expect, it } from 'vitest'
import { StatusBadge } from './StatusBadge'

describe('StatusBadge', () => {
  it('renders the metric state', () => {
    render(<StatusBadge status="ROJO" />)
    expect(screen.getByText('ROJO')).toBeTruthy()
  })
})

