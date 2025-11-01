import React, { useEffect, useState } from 'react';
import { getDashboardStats } from '../services/api';
import { 
  ShieldCheckIcon, 
  ExclamationTriangleIcon, 
  ChartBarIcon, 
  ClockIcon 
} from '@heroicons/react/24/outline';

const Dashboard = () => {
  const [stats, setStats] = useState({
    total_scans: 0,
    total_vulnerabilities: 0,
    critical_vulnerabilities: 0,
    active_sca
