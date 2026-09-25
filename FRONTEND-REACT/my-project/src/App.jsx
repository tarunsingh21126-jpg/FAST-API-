import { Component, useState } from 'react'
import JobCard from "./components/JobCard";
import jobs from "./data/jobs";

function App() {
  return (
    <main className="min-h-screen bg-white px-5 py-8 md:px-10 lg:px-16">

      {/* Header */}
      <div className="mx-auto mb-8 max-w-7xl">

        <p className="mb-2 text-sm font-medium text-gray-400">
          FIND YOUR NEXT OPPORTUNITY
        </p>

        <h1 className="text-3xl font-semibold tracking-tight text-gray-900 md:text-4xl">
          Job Applications
        </h1>

      </div>

      {/* Job Grid */}
      <section className="mx-auto grid max-w-7xl grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3">

        {jobs.map((job) => (
          <JobCard
            key={job.id}
            job={job}
          />
        ))}

      </section>

    </main>
  );
}

export default App;