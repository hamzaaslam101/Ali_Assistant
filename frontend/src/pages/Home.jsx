import React, { useState } from 'react';
import Dashboard from '../components/Dashboard';
import Chat from '../components/Chat';
import ScanResults from '../components/ScanResults';
import ReconPanel from '../components/ReconPanel';
import { ArrowRightOnRectangleIcon } from '@heroicons/react/24/outline';
import { logout } from '../services/api';

const Home = () => {
  const [activeTab, setActiveTab] = useState('dashboard');

  const handleLogout = () => {
    logout();
    window.location.href = '/login';
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900">
      {/* Header */}
      <header className="bg-gray-800 border-b border-gray-700 shadow-lg">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center py-4">
            <div className="flex items-center">
              <h1 className="text-3xl font-bold bg-gradient-to-r from-blue-500 to-purple-600 bg-clip-text text-transparent">
                🛡️ Ali Security Engineer
              </h1>
              <span className="ml-3 px-3 py-1 bg-blue-600 text-white text-xs font-semibold rounded-full">
                AI-Powered
              </span>
            </div>
            <button
              onClick={handleLogout}
              className="flex items-center space-x-2 px-4 py-2 bg-red-600 hover:bg-red-700 text-white rounded-lg transition-colors"
            >
              <ArrowRightOnRectangleIcon className="h-5 w-5" />
              <span>Logout</span>
            </button>
          </div>
        </div>
      </header>

      {/* Navigation Tabs */}
      <div className="bg-gray-800 border-b border-gray-700">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <nav className="flex space-x-4">
            {[
              { id: 'dashboard', label: 'Dashbo
